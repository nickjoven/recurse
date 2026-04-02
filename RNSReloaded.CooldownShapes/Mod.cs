using System.Runtime.InteropServices;
using Reloaded.Hooks.Definitions;
using Reloaded.Mod.Interfaces;
using Reloaded.Mod.Interfaces.Internal;
using RNSReloaded.CooldownShapes.Config;
using RNSReloaded.CooldownShapes.Drawing;
using RNSReloaded.CooldownShapes.Shapes;
using RNSReloaded.Interfaces;
using RNSReloaded.Interfaces.Structs;

namespace RNSReloaded.CooldownShapes;

public unsafe class Mod : IMod {
    private WeakReference<IRNSReloaded>? _rnsRef;
    private WeakReference<IReloadedHooks>? _hooksRef;
    private ILoggerV1 _logger = null!;

    private Configurator _configurator = null!;
    private Config.Config _config = null!;

    private GMDraw? _gm;
    private CooldownReader? _reader;
    private IHook<ScriptDelegate>? _drawHook;
    private IHook<ScriptDelegate>? _hotbarUsedHook;
    private IHook<ScriptDelegate>? _cooldownAddHook;

    // Track last-used ability per slot for debugging/correlation
    private readonly Dictionary<int, double> _lastHotbarUseTime = new();

    // Frame tracking — reset _drawnThisFrame when gametime advances
    private int _frameCount;
    private bool _drawnThisFrame;
    private double _lastDrawGametime = -1;
    private const int DiscoveryLogInterval = 300;
    private HashSet<string> _discoveredDrawEvents = new();

    public void StartEx(IModLoaderV1 loader, IModConfigV1 modConfig) {
        _rnsRef = loader.GetController<IRNSReloaded>();
        _hooksRef = loader.GetController<IReloadedHooks>()!;
        _logger = loader.GetLogger();

        _configurator = new Configurator(((IModLoader)loader).GetModConfigDirectory(modConfig.ModId));
        _config = _configurator.GetConfiguration<Config.Config>(0);
        _config.ConfigurationUpdated += c => _config = (Config.Config)c;

        if (_rnsRef!.TryGetTarget(out var rns)) {
            rns.OnReady += Ready;
        }
    }

    private void Ready() {
        if (!_rnsRef!.TryGetTarget(out var rns)) return;
        if (!_hooksRef!.TryGetTarget(out var hooks)) return;

        _gm = new GMDraw(rns);
        _reader = new CooldownReader(rns);

        // Strategy 1: Hook a specific draw script if configured
        if (!string.IsNullOrEmpty(_config.DrawHookScript)) {
            HookDrawScript(rns, hooks, _config.DrawHookScript);
        }

        // Hook hotbar triggers to track ability activations
        HookScript(rns, hooks, "hotbarUsed", HotbarUsedDetour, ref _hotbarUsedHook);
        HookScript(rns, hooks, "hotbarUsedProc", HotbarUsedDetour, ref _hotbarUsedHook);

        // Hook the game's own cooldown manipulation to observe CD changes
        HookScript(rns, hooks, "tpat_hb_add_cooldown", CooldownAddDetour, ref _cooldownAddHook);

        // Strategy 2: Use OnExecuteIt to piggyback on any per-frame script
        // This fires on every script execution — we draw after HUD-related scripts
        rns.OnExecuteIt += OnExecuteIt;

        _logger.PrintMessage("[CooldownShapes] Ready. Shape=" + _config.Shape +
            ", Discovery=" + _config.DiscoveryMode, _logger.ColorGreenLight);
    }

    private void HookDrawScript(IRNSReloaded rns, IReloadedHooks hooks, string scriptName) {
        try {
            var id = rns.ScriptFindId(scriptName);
            var script = rns.GetScriptData(id - 100000);
            _drawHook = hooks.CreateHook<ScriptDelegate>(DrawDetour, script->Functions->Function);
            _drawHook.Activate();
            _drawHook.Enable();
            _logger.PrintMessage("[CooldownShapes] Hooked draw script: " + scriptName, _logger.ColorGreenLight);
        } catch (Exception e) {
            _logger.PrintMessage("[CooldownShapes] Failed to hook '" + scriptName + "': " + e.Message, _logger.ColorRed);
        }
    }

    private void HookScript(IRNSReloaded rns, IReloadedHooks hooks, string scriptName,
                             ScriptDelegate detour, ref IHook<ScriptDelegate>? hookField) {
        try {
            var id = rns.ScriptFindId(scriptName);
            var script = rns.GetScriptData(id - 100000);
            hookField = hooks.CreateHook<ScriptDelegate>(detour, script->Functions->Function);
            hookField.Activate();
            hookField.Enable();
            _logger.PrintMessage("[CooldownShapes] Hooked: " + scriptName, _logger.ColorGreenLight);
        } catch {
            // Script may not exist — non-fatal
            _logger.PrintMessage("[CooldownShapes] Script not found (non-fatal): " + scriptName, _logger.ColorYellowLight);
        }
    }

    /// <summary>Fires when an ability is used from the hotbar. Logs for discovery.</summary>
    private RValue* HotbarUsedDetour(CInstance* self, CInstance* other, RValue* returnValue, int argc, RValue** argv) {
        if (_config.DiscoveryMode && _rnsRef!.TryGetTarget(out var rns)) {
            var playerId = TryReadLong(rns, self, "playerId");
            var hbId = TryReadLong(rns, self, "hbId");
            var gt = _reader?.GetGlobalDouble("gametime");
            _logger.PrintMessage(
                $"[CooldownShapes:Discovery] hotbarUsed: player={playerId}, hbId={hbId}, gametime={gt}",
                _logger.ColorYellowLight);

            if (hbId != null) {
                _lastHotbarUseTime[(int)hbId.Value] = gt ?? 0;
            }
        }
        return _hotbarUsedHook!.OriginalFunction(self, other, returnValue, argc, argv);
    }

    /// <summary>Fires when the game adds/reduces cooldown on an ability. Logs for discovery.</summary>
    private RValue* CooldownAddDetour(CInstance* self, CInstance* other, RValue* returnValue, int argc, RValue** argv) {
        if (_config.DiscoveryMode && _rnsRef!.TryGetTarget(out var rns)) {
            string args = "";
            for (int i = 0; i < argc; i++) {
                args += (i > 0 ? ", " : "") + argv[i]->ToString();
            }
            _logger.PrintMessage(
                $"[CooldownShapes:Discovery] tpat_hb_add_cooldown({args})",
                _logger.ColorYellowLight);
        }
        return _cooldownAddHook!.OriginalFunction(self, other, returnValue, argc, argv);
    }

    private long? TryReadLong(IRNSReloaded rns, CInstance* inst, string varName) {
        try {
            var val = rns.FindValue(inst, varName);
            if (val == null) return null;
            return rns.utils.RValueToLong(val);
        } catch {
            return null;
        }
    }

    private RValue* DrawDetour(CInstance* self, CInstance* other, RValue* returnValue, int argc, RValue** argv) {
        // Call original first
        returnValue = _drawHook!.OriginalFunction(self, other, returnValue, argc, argv);

        // Then draw our indicators on top
        RenderCooldowns(self, other);

        return returnValue;
    }

    private void OnExecuteIt(ExecuteItArguments args) {
        _frameCount++;

        // OnExecuteIt fires on EVERY GML code execution. Filter by code name
        // to only draw during a Draw event (safe context for GM draw calls).
        // args.Code->Name gives us e.g. "gml_Object_obj_battlecontroller_Draw_0"
        string? codeName = null;
        try {
            codeName = Marshal.PtrToStringAnsi((nint)args.Code->Name);
        } catch {
            return;
        }

        // Discovery mode: log code names to find the right draw event
        if (_config.DiscoveryMode) {
            if (codeName != null && codeName.Contains("Draw") && _discoveredDrawEvents.Add(codeName)) {
                _logger.PrintMessage($"[CooldownShapes:Discovery] Draw event: {codeName}", _logger.ColorYellowLight);
            }
            if (_frameCount % DiscoveryLogInterval == 0) {
                LogDiscoveryInfo();
            }
        }

        // If we have a dedicated draw hook, don't also draw from OnExecuteIt
        if (_drawHook != null) return;

        // Only draw during a Draw event — look for configurable pattern or default
        if (codeName == null) return;
        string drawFilter = !string.IsNullOrEmpty(_config.DrawEventFilter)
            ? _config.DrawEventFilter
            : "Draw";
        if (!codeName.Contains(drawFilter)) return;

        // Avoid drawing multiple times per frame if multiple draw events match
        if (_drawnThisFrame) return;
        _drawnThisFrame = true;

        RenderCooldowns(args.Self, args.Other);
    }

    private void RenderCooldowns(CInstance* self, CInstance* other) {
        if (_gm == null || _reader == null) return;
        if (!_rnsRef!.TryGetTarget(out var rns)) return;

        // Reset once-per-frame flag when gametime advances
        var gt = _reader.GetGlobalDouble("gametime") ?? 0;
        if (gt != _lastDrawGametime) {
            _drawnThisFrame = false;
            _lastDrawGametime = gt;
        }

        _gm.BeginFrame(self, other);

        var shape = ShapeFactory.Get(_config.Shape);
        var style = _config.ToShapeStyle();
        int count = Math.Clamp(_config.SlotCount, 1, 8);

        for (int i = 0; i < count; i++) {
            double x, y;
            if (_config.Direction == LayoutDirection.Horizontal) {
                x = _config.AnchorX + i * _config.Spacing;
                y = _config.AnchorY;
            } else {
                x = _config.AnchorX;
                y = _config.AnchorY + i * _config.Spacing;
            }

            var slot = _config.SlotForIndex(i);
            double progress = _reader.ReadSlotProgress(_config.PlayerIndex, slot) ?? 1.0;

            shape.Draw(_gm, x, y, _config.Size, progress, style);
        }

        // Restore draw state
        _gm.SetAlpha(1.0);
        _gm.SetColor(GMDraw.ColorRGB(255, 255, 255));
    }

    private void LogDiscoveryInfo() {
        if (!_rnsRef!.TryGetTarget(out var rns)) return;

        _logger.PrintMessage("[CooldownShapes:Discovery] --- Frame " + _frameCount + " ---", _logger.ColorYellowLight);

        // Log gametime
        var gt = _reader?.GetGlobalDouble("gametime");
        if (gt != null) {
            _logger.PrintMessage("  gametime = " + gt.Value, _logger.ColorYellowLight);
        }

        // Try to read configured cooldown vars for player 0
        for (int i = 0; i < Math.Min(_config.SlotCount, 4); i++) {
            var slot = _config.SlotForIndex(i);
            var cur = _reader?.GetPlayerDouble(_config.PlayerIndex, slot.CurrentVarName);
            var max = _reader?.GetPlayerDouble(_config.PlayerIndex, slot.MaxVarName);
            _logger.PrintMessage(
                $"  Slot {i}: {slot.CurrentVarName}={cur?.ToString() ?? "null"}, " +
                $"{slot.MaxVarName}={max?.ToString() ?? "null"}",
                cur != null ? _logger.ColorGreenLight : _logger.ColorRed
            );
        }

        // Probe known and likely variable names from R&S internals
        // GCD = global cooldown (locks all abilities), CD = per-ability recast
        string[] candidates = {
            // GCD-related
            "gcd", "gcdMax", "gcdTimer", "gcdLength",
            "globalCooldown", "globalCooldownMax",
            // Per-ability cooldown/recast
            "cooldown", "cooldownMax", "cd", "cdMax",
            "hbCooldown", "hbCooldownMax",
            "recast", "recastMax", "recastTimer",
            // Hotbar / ability identifiers (context)
            "hbId", "playerId", "hbsUniqueId",
            // Stock/charge system
            "stock", "stockGcd", "stockMax",
            // Cast/animation timing
            "castTime", "castTimeMax",
            "windup", "recovery",
            // Status/buff system (for HoT/DoT cooldowns)
            "statusId", "initLength", "strength",
            // Invuln / defensive cooldowns
            "invulnTimer", "invulnLength",
        };
        foreach (var name in candidates) {
            var val = _reader?.GetPlayerDouble(_config.PlayerIndex, name);
            if (val != null) {
                _logger.PrintMessage($"  FOUND: {name} = {val.Value}", _logger.ColorGreenLight);
            }
        }

        // Also log any recent hotbar activations
        if (_lastHotbarUseTime.Count > 0) {
            _logger.PrintMessage("  Recent hotbar uses:", _logger.ColorYellowLight);
            foreach (var (hbId, time) in _lastHotbarUseTime) {
                _logger.PrintMessage($"    hbId={hbId} at gametime={time}", _logger.ColorYellowLight);
            }
        }
    }

    // --- Lifecycle ---

    public void Suspend() { }
    public void Resume() { }
    public bool CanSuspend() => true;
    public void Unload() { }
    public bool CanUnload() => false;
    public Action Disposing => () => { };
}

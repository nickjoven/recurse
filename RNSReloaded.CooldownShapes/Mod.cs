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

    // Discovery mode throttle — log every N frames
    private int _frameCount;
    private const int DiscoveryLogInterval = 300;
    private HashSet<string> _discoveredScripts = new();

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

    private RValue* DrawDetour(CInstance* self, CInstance* other, RValue* returnValue, int argc, RValue** argv) {
        // Call original first
        returnValue = _drawHook!.OriginalFunction(self, other, returnValue, argc, argv);

        // Then draw our indicators on top
        RenderCooldowns(self, other);

        return returnValue;
    }

    private void OnExecuteIt(ExecuteItArguments args) {
        _frameCount++;

        // Discovery mode: log script names periodically to help find the right hook point
        if (_config.DiscoveryMode && _frameCount % DiscoveryLogInterval == 0) {
            LogDiscoveryInfo();
        }

        // If we have a dedicated draw hook, don't also draw from OnExecuteIt
        if (_drawHook != null) return;

        // Without a hook, we draw on every OnExecuteIt call.
        // This will fire many times per frame — use the global instance as context.
        // A better approach is to configure DrawHookScript once you discover the right one.
        if (_frameCount % 2 == 0) return; // throttle: draw every other call

        if (!_rnsRef!.TryGetTarget(out var rns)) return;
        var global = rns.GetGlobalInstance();
        RenderCooldowns(global, global);
    }

    private void RenderCooldowns(CInstance* self, CInstance* other) {
        if (_gm == null || _reader == null) return;
        if (!_rnsRef!.TryGetTarget(out var rns)) return;

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

        // Try some likely candidate variable names
        string[] candidates = {
            "cooldown", "cooldownMax", "cd", "cdMax",
            "hbCooldown", "hbCooldownMax",
            "abilityCooldown", "abilityCooldownMax",
            "gcd", "gcdMax", "castTime", "castTimeMax",
            "skillCooldown", "skillCooldownMax",
        };
        foreach (var name in candidates) {
            var val = _reader?.GetPlayerDouble(_config.PlayerIndex, name);
            if (val != null) {
                _logger.PrintMessage($"  FOUND: {name} = {val.Value}", _logger.ColorGreenLight);
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

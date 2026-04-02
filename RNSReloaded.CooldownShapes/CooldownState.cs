using RNSReloaded.Interfaces;
using RNSReloaded.Interfaces.Structs;

namespace RNSReloaded.CooldownShapes;

/// <summary>
/// Reads ability cooldown state from the game.
///
/// R&amp;S ability cooldowns are tracked per-player. The exact variable names
/// depend on game version. This reader is configurable: you set the variable
/// names via SlotConfig and it probes the game state each frame.
///
/// Discovery mode: when enabled, dumps all accessible player variable names
/// to the Reloaded log so you can find the right cooldown fields.
/// </summary>
public unsafe class CooldownReader {
    private readonly IRNSReloaded _rns;

    public CooldownReader(IRNSReloaded rns) {
        _rns = rns;
    }

    /// <summary>
    /// Read cooldown progress for a specific ability slot of a specific player.
    /// Returns 0.0 (fully on cooldown) to 1.0 (ready).
    /// Returns null if the variable couldn't be read.
    /// </summary>
    public double? ReadSlotProgress(int playerIndex, SlotConfig slot) {
        // Try reading current cooldown and max cooldown from player vars
        var current = GetPlayerDouble(playerIndex, slot.CurrentVarName);
        var max = GetPlayerDouble(playerIndex, slot.MaxVarName);

        if (current == null || max == null || max.Value <= 0.0)
            return null;

        // Progress: 1.0 when current reaches 0 (or equals max depending on convention)
        // Convention A: current counts DOWN from max to 0 → progress = 1 - (current/max)
        // Convention B: current counts UP from 0 to max → progress = current/max
        // Configurable per slot
        double ratio = current.Value / max.Value;
        return slot.CountsDown ? 1.0 - ratio : ratio;
    }

    /// <summary>
    /// Read a raw double from a player variable. Returns null on failure.
    /// </summary>
    public double? GetPlayerDouble(int playerIndex, string varName) {
        if (string.IsNullOrEmpty(varName)) return null;
        try {
            var val = _rns.utils.GetPlayerVar(playerIndex, varName);
            if (val == null) return null;
            return _rns.utils.RValueToDouble(val);
        } catch {
            return null;
        }
    }

    /// <summary>
    /// Read a raw double from a global variable. Returns null on failure.
    /// </summary>
    public double? GetGlobalDouble(string varName) {
        if (string.IsNullOrEmpty(varName)) return null;
        try {
            var val = _rns.FindValue(_rns.GetGlobalInstance(), varName);
            if (val == null) return null;
            return _rns.utils.RValueToDouble(val);
        } catch {
            return null;
        }
    }

    /// <summary>
    /// Attempt to enumerate struct keys on a player variable (for discovery).
    /// </summary>
    public List<string>? InspectPlayerVar(int playerIndex, string varName) {
        try {
            var val = _rns.utils.GetPlayerVar(playerIndex, varName);
            if (val == null) return null;
            return _rns.GetStructKeys(val);
        } catch {
            return null;
        }
    }
}

/// <summary>
/// Configuration for one ability/cooldown slot.
/// </summary>
public struct SlotConfig {
    /// <summary>Player variable name for the current cooldown value.</summary>
    public string CurrentVarName;

    /// <summary>Player variable name for the max cooldown value.</summary>
    public string MaxVarName;

    /// <summary>If true, the current value counts down from max to 0.</summary>
    public bool CountsDown;

    /// <summary>Display label (for debugging/logging).</summary>
    public string Label;

    public static SlotConfig Create(string current, string max, bool countsDown = true, string label = "") =>
        new SlotConfig {
            CurrentVarName = current,
            MaxVarName = max,
            CountsDown = countsDown,
            Label = label,
        };
}

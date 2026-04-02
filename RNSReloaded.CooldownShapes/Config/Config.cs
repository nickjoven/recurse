using System.ComponentModel;
using RNSReloaded.CooldownShapes.Drawing;
using RNSReloaded.CooldownShapes.Shapes;
using Reloaded.Mod.Interfaces;

namespace RNSReloaded.CooldownShapes.Config;

public class Config : Configurable<Config> {
    // --- Layout ---

    [DisplayName("Shape Type")]
    [Description("Geometric shape for cooldown indicators: Ring, Cross, X, DiamondGrid, DotArray")]
    [DefaultValue(ShapeType.Ring)]
    public ShapeType Shape { get; set; } = ShapeType.Ring;

    [DisplayName("Shape Size")]
    [Description("Size of each indicator in pixels")]
    [DefaultValue(32.0)]
    public double Size { get; set; } = 32.0;

    [DisplayName("Anchor X")]
    [Description("X position of the first indicator (pixels from left)")]
    [DefaultValue(120.0)]
    public double AnchorX { get; set; } = 120.0;

    [DisplayName("Anchor Y")]
    [Description("Y position of the first indicator (pixels from top)")]
    [DefaultValue(680.0)]
    public double AnchorY { get; set; } = 680.0;

    [DisplayName("Spacing")]
    [Description("Pixels between indicator centers")]
    [DefaultValue(40.0)]
    public double Spacing { get; set; } = 40.0;

    [DisplayName("Layout Direction")]
    [Description("Horizontal or Vertical arrangement")]
    [DefaultValue(LayoutDirection.Horizontal)]
    public LayoutDirection Direction { get; set; } = LayoutDirection.Horizontal;

    // --- Colors (GM BGR as integer, or use the RGB helper) ---

    [DisplayName("Ready Color (BGR)")]
    [Description("Color when ability is off cooldown. BGR integer.")]
    [DefaultValue(13172364)] // ~GMDraw.ColorRGB(140, 255, 200)
    public double ReadyColor { get; set; } = GMDraw.ColorRGB(140, 255, 200);

    [DisplayName("Active Color (BGR)")]
    [Description("Color for the filling portion during cooldown. BGR integer.")]
    [DefaultValue(15789276)] // ~GMDraw.ColorRGB(220, 220, 240)
    public double ActiveColor { get; set; } = GMDraw.ColorRGB(220, 220, 240);

    [DisplayName("Background Color (BGR)")]
    [Description("Color for the unfilled background. BGR integer.")]
    [DefaultValue(3289640)] // ~GMDraw.ColorRGB(40, 40, 50)
    public double BackgroundColor { get; set; } = GMDraw.ColorRGB(40, 40, 50);

    [DisplayName("Active Alpha")]
    [DefaultValue(0.9)]
    public double ActiveAlpha { get; set; } = 0.9;

    [DisplayName("Background Alpha")]
    [DefaultValue(0.3)]
    public double BackgroundAlpha { get; set; } = 0.3;

    [DisplayName("Line Width")]
    [DefaultValue(2.0)]
    public double LineWidth { get; set; } = 2.0;

    [DisplayName("Arc Segments / Dot Count")]
    [Description("Ring arc resolution, or number of dots for DotArray")]
    [DefaultValue(24)]
    public int Segments { get; set; } = 24;

    // --- Cooldown variable mapping ---

    [DisplayName("Slot Count")]
    [Description("Number of ability slots to track (1-8)")]
    [DefaultValue(4)]
    public int SlotCount { get; set; } = 4;

    [DisplayName("Cooldown Current Var Pattern")]
    [Description("Player variable name pattern for current cooldown value. Use {i} for slot index (0-based). Example: hbCooldown{i}")]
    [DefaultValue("hbCooldown{i}")]
    public string CooldownCurrentPattern { get; set; } = "hbCooldown{i}";

    [DisplayName("Cooldown Max Var Pattern")]
    [Description("Player variable name pattern for max cooldown value. Use {i} for slot index. Example: hbCooldownMax{i}")]
    [DefaultValue("hbCooldownMax{i}")]
    public string CooldownMaxPattern { get; set; } = "hbCooldownMax{i}";

    [DisplayName("Cooldown Counts Down")]
    [Description("If true, current value decreases from max to 0. If false, it increases from 0 to max.")]
    [DefaultValue(true)]
    public bool CooldownCountsDown { get; set; } = true;

    // --- Hook target ---

    [DisplayName("Draw Hook Script")]
    [Description("GML script name to hook for per-frame drawing. Leave empty to use OnExecuteIt with draw event filter.")]
    [DefaultValue("")]
    public string DrawHookScript { get; set; } = "";

    [DisplayName("Draw Event Filter")]
    [Description("Substring to match in OnExecuteIt code names for draw context. Default 'Draw' matches any Draw event. Discovery mode logs all draw events it finds.")]
    [DefaultValue("Draw")]
    public string DrawEventFilter { get; set; } = "Draw";

    // --- Debug ---

    [DisplayName("Discovery Mode")]
    [Description("When enabled, logs available script names and player variables to help find cooldown data.")]
    [DefaultValue(false)]
    public bool DiscoveryMode { get; set; } = false;

    [DisplayName("Player Index")]
    [Description("Which player to read cooldowns from (0 = local player).")]
    [DefaultValue(0)]
    public int PlayerIndex { get; set; } = 0;

    // --- Helpers ---

    public ShapeStyle ToShapeStyle() => new ShapeStyle {
        ReadyColor = ReadyColor,
        ActiveColor = ActiveColor,
        BackgroundColor = BackgroundColor,
        ActiveAlpha = ActiveAlpha,
        BackgroundAlpha = BackgroundAlpha,
        LineWidth = LineWidth,
        Segments = Segments,
    };

    public SlotConfig SlotForIndex(int i) => SlotConfig.Create(
        current: CooldownCurrentPattern.Replace("{i}", i.ToString()),
        max: CooldownMaxPattern.Replace("{i}", i.ToString()),
        countsDown: CooldownCountsDown,
        label: $"Slot {i}"
    );
}

public enum LayoutDirection {
    Horizontal,
    Vertical,
}

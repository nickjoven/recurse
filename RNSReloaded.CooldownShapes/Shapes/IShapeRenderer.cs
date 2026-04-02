using RNSReloaded.CooldownShapes.Drawing;

namespace RNSReloaded.CooldownShapes.Shapes;

/// <summary>
/// Renders a single cooldown indicator at a given position.
/// Progress ranges from 0.0 (fully on cooldown) to 1.0 (ready).
/// </summary>
public interface IShapeRenderer {
    void Draw(GMDraw gm, double cx, double cy, double size, double progress, ShapeStyle style);
}

/// <summary>Visual style for a cooldown shape.</summary>
public struct ShapeStyle {
    /// <summary>GM BGR color when the ability is ready (progress = 1).</summary>
    public double ReadyColor;

    /// <summary>GM BGR color for the active/filling portion during cooldown.</summary>
    public double ActiveColor;

    /// <summary>GM BGR color for the unfilled/background portion.</summary>
    public double BackgroundColor;

    /// <summary>Alpha for the filled portion (0-1).</summary>
    public double ActiveAlpha;

    /// <summary>Alpha for the background portion (0-1).</summary>
    public double BackgroundAlpha;

    /// <summary>Line width for outline-based shapes.</summary>
    public double LineWidth;

    /// <summary>Number of segments for curved shapes (ring arc resolution).</summary>
    public int Segments;

    public static ShapeStyle Default => new ShapeStyle {
        ReadyColor = GMDraw.ColorRGB(140, 255, 200),   // soft green
        ActiveColor = GMDraw.ColorRGB(220, 220, 240),   // cool white
        BackgroundColor = GMDraw.ColorRGB(40, 40, 50),   // dark grey
        ActiveAlpha = 0.9,
        BackgroundAlpha = 0.3,
        LineWidth = 2.0,
        Segments = 24,
    };
}

public enum ShapeType {
    Ring,
    Cross,
    X,
    DiamondGrid,
    DotArray,
}

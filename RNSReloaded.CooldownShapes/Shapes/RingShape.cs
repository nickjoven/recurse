using RNSReloaded.CooldownShapes.Drawing;

namespace RNSReloaded.CooldownShapes.Shapes;

/// <summary>
/// Radial ring that sweeps clockwise from 12 o'clock.
/// At progress=0 the ring is fully dim; at progress=1 it's fully lit.
/// Uses a triangle-fan arc for the filled portion and a full circle outline behind it.
/// </summary>
public class RingShape : IShapeRenderer {
    public void Draw(GMDraw gm, double cx, double cy, double size, double progress, ShapeStyle style) {
        double radius = size * 0.5;
        double inner = radius * 0.7;
        int segments = Math.Max(8, style.Segments);

        // Background: full ring (dim)
        DrawArc(gm, cx, cy, inner, radius, 0.0, 1.0, segments,
                style.BackgroundColor, style.BackgroundAlpha);

        if (progress <= 0.0) return;

        // Foreground: partial arc based on progress
        double color = progress >= 1.0 ? style.ReadyColor : style.ActiveColor;
        double alpha = style.ActiveAlpha;
        DrawArc(gm, cx, cy, inner, radius, 0.0, Math.Min(progress, 1.0), segments,
                color, alpha);
    }

    private static void DrawArc(
        GMDraw gm, double cx, double cy,
        double innerR, double outerR,
        double startFrac, double endFrac, int segments,
        double color, double alpha
    ) {
        // Sweep from 12 o'clock (-PI/2) clockwise
        double startAngle = -Math.PI / 2.0 + startFrac * Math.PI * 2.0;
        double endAngle = -Math.PI / 2.0 + endFrac * Math.PI * 2.0;
        double step = (endAngle - startAngle) / segments;

        gm.SetColor(color);
        gm.SetAlpha(alpha);
        gm.PrimitiveBegin(PrimitiveKind.TriangleStrip);

        for (int i = 0; i <= segments; i++) {
            double angle = startAngle + step * i;
            double cos = Math.Cos(angle);
            double sin = Math.Sin(angle);
            gm.Vertex(cx + cos * innerR, cy + sin * innerR);
            gm.Vertex(cx + cos * outerR, cy + sin * outerR);
        }

        gm.PrimitiveEnd();
    }
}

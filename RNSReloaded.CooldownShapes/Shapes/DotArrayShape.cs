using RNSReloaded.CooldownShapes.Drawing;

namespace RNSReloaded.CooldownShapes.Shapes;

/// <summary>
/// Array of discrete dots/pips arranged in a ring pattern.
/// Each pip lights up as progress passes its threshold.
/// Configurable via Segments (dot count) in ShapeStyle.
/// </summary>
public class DotArrayShape : IShapeRenderer {
    public void Draw(GMDraw gm, double cx, double cy, double size, double progress, ShapeStyle style) {
        int dotCount = Math.Max(4, style.Segments);
        double ringRadius = size * 0.38;
        double dotRadius = size * 0.08;
        double startAngle = -Math.PI / 2.0; // 12 o'clock

        for (int i = 0; i < dotCount; i++) {
            double frac = (double)i / dotCount;
            double angle = startAngle + frac * Math.PI * 2.0;
            double dx = cx + Math.Cos(angle) * ringRadius;
            double dy = cy + Math.Sin(angle) * ringRadius;

            bool lit = progress > frac;

            if (lit) {
                double color = progress >= 1.0 ? style.ReadyColor : style.ActiveColor;
                gm.SetColor(color);
                gm.SetAlpha(style.ActiveAlpha);
            } else {
                gm.SetColor(style.BackgroundColor);
                gm.SetAlpha(style.BackgroundAlpha);
            }

            gm.Circle(dx, dy, dotRadius, false);
        }
    }
}

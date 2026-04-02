using RNSReloaded.CooldownShapes.Drawing;

namespace RNSReloaded.CooldownShapes.Shapes;

/// <summary>
/// Plus (+) shape with 4 arms extending from center.
/// Arms fill outward from center as progress increases.
/// Each arm covers 25% of total progress (up/right/down/left).
/// </summary>
public class CrossShape : IShapeRenderer {
    public void Draw(GMDraw gm, double cx, double cy, double size, double progress, ShapeStyle style) {
        double halfArm = size * 0.45;
        double thickness = Math.Max(style.LineWidth, size * 0.12);
        double halfT = thickness * 0.5;

        // Background: full cross
        DrawArms(gm, cx, cy, halfArm, halfT, 1.0, style.BackgroundColor, style.BackgroundAlpha);

        if (progress <= 0.0) return;

        // Foreground: arms fill sequentially
        double color = progress >= 1.0 ? style.ReadyColor : style.ActiveColor;
        DrawArms(gm, cx, cy, halfArm, halfT, Math.Min(progress, 1.0), color, style.ActiveAlpha);
    }

    private static void DrawArms(
        GMDraw gm, double cx, double cy,
        double halfArm, double halfT, double progress,
        double color, double alpha
    ) {
        gm.SetColor(color);
        gm.SetAlpha(alpha);

        // 4 arms: up, right, down, left — each gets 25% of progress
        (double dx, double dy)[] dirs = { (0, -1), (1, 0), (0, 1), (-1, 0) };

        for (int i = 0; i < 4; i++) {
            double armProgress = Math.Clamp((progress - i * 0.25) / 0.25, 0.0, 1.0);
            if (armProgress <= 0.0) continue;

            double len = halfArm * armProgress;
            double dx = dirs[i].dx;
            double dy = dirs[i].dy;

            // Perpendicular for thickness
            double px = -dy * halfT;
            double py = dx * halfT;

            // Arm rectangle from center outward
            double x1, y1, x2, y2;
            if (Math.Abs(dx) > 0.5) {
                // Horizontal arm
                x1 = cx;
                x2 = cx + dx * len;
                y1 = cy - halfT;
                y2 = cy + halfT;
            } else {
                // Vertical arm
                x1 = cx - halfT;
                x2 = cx + halfT;
                y1 = cy;
                y2 = cy + dy * len;
            }

            // Normalize so x1 < x2, y1 < y2
            gm.Rectangle(Math.Min(x1, x2), Math.Min(y1, y2),
                          Math.Max(x1, x2), Math.Max(y1, y2), false);
        }
    }
}

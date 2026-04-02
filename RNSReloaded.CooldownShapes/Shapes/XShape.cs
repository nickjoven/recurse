using RNSReloaded.CooldownShapes.Drawing;

namespace RNSReloaded.CooldownShapes.Shapes;

/// <summary>
/// X shape — a 45-degree rotated cross. Same fill logic as CrossShape
/// but arms extend diagonally (NE, SE, SW, NW).
/// </summary>
public class XShape : IShapeRenderer {
    public void Draw(GMDraw gm, double cx, double cy, double size, double progress, ShapeStyle style) {
        double halfArm = size * 0.4;
        double w = Math.Max(style.LineWidth, size * 0.1);

        // Background
        DrawArms(gm, cx, cy, halfArm, w, 1.0, style.BackgroundColor, style.BackgroundAlpha);

        if (progress <= 0.0) return;

        double color = progress >= 1.0 ? style.ReadyColor : style.ActiveColor;
        DrawArms(gm, cx, cy, halfArm, w, Math.Min(progress, 1.0), color, style.ActiveAlpha);
    }

    private static void DrawArms(
        GMDraw gm, double cx, double cy,
        double halfArm, double w, double progress,
        double color, double alpha
    ) {
        gm.SetColor(color);
        gm.SetAlpha(alpha);

        double diag = 1.0 / Math.Sqrt(2.0);
        (double dx, double dy)[] dirs = {
            ( diag, -diag), // NE
            ( diag,  diag), // SE
            (-diag,  diag), // SW
            (-diag, -diag), // NW
        };

        for (int i = 0; i < 4; i++) {
            double armProgress = Math.Clamp((progress - i * 0.25) / 0.25, 0.0, 1.0);
            if (armProgress <= 0.0) continue;

            double len = halfArm * armProgress;
            double ex = cx + dirs[i].dx * len;
            double ey = cy + dirs[i].dy * len;
            gm.LineWidth(cx, cy, ex, ey, w);
        }
    }
}

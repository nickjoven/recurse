using RNSReloaded.CooldownShapes.Drawing;

namespace RNSReloaded.CooldownShapes.Shapes;

/// <summary>
/// Tilted 2x2 diamond grid. Four diamond cells arranged in a square rotated 45 degrees.
/// Cells light up sequentially as progress increases (each cell = 25%).
/// Fill order: top, right, bottom, left (clockwise from 12 o'clock).
/// </summary>
public class DiamondGridShape : IShapeRenderer {
    public void Draw(GMDraw gm, double cx, double cy, double size, double progress, ShapeStyle style) {
        double cellSize = size * 0.28;
        double gap = size * 0.04;
        double offset = cellSize + gap;

        // Cell centers relative to (cx, cy) — arranged as a diamond (rotated square)
        (double dx, double dy)[] cells = {
            ( 0, -offset), // top
            ( offset,  0), // right
            ( 0,  offset), // bottom
            (-offset,  0), // left
        };

        for (int i = 0; i < 4; i++) {
            double cellProgress = Math.Clamp((progress - i * 0.25) / 0.25, 0.0, 1.0);
            double ccx = cx + cells[i].dx;
            double ccy = cy + cells[i].dy;

            // Background diamond (always)
            DrawDiamond(gm, ccx, ccy, cellSize, style.BackgroundColor, style.BackgroundAlpha);

            // Filled diamond (based on this cell's progress)
            if (cellProgress > 0.0) {
                double color = (progress >= 1.0) ? style.ReadyColor : style.ActiveColor;
                double fillSize = cellSize * cellProgress;
                DrawDiamond(gm, ccx, ccy, fillSize, color, style.ActiveAlpha);
            }
        }
    }

    private static void DrawDiamond(GMDraw gm, double cx, double cy, double halfSize, double color, double alpha) {
        gm.SetColor(color);
        gm.SetAlpha(alpha);
        gm.PrimitiveBegin(PrimitiveKind.TriangleFan);
        gm.Vertex(cx, cy - halfSize); // top
        gm.Vertex(cx + halfSize, cy); // right
        gm.Vertex(cx, cy + halfSize); // bottom
        gm.Vertex(cx - halfSize, cy); // left
        gm.PrimitiveEnd();
    }
}

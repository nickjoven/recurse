using RNSReloaded.Interfaces;
using RNSReloaded.Interfaces.Structs;

namespace RNSReloaded.CooldownShapes.Drawing;

/// <summary>
/// Thin wrapper over GameMaker draw built-ins, called via ExecuteCodeFunction.
/// All coordinates are in GM room-space. Colors are 24-bit BGR integers.
/// </summary>
public unsafe class GMDraw {
    private readonly IRNSReloaded _rns;
    private CInstance* _self;
    private CInstance* _other;

    public GMDraw(IRNSReloaded rns) {
        _rns = rns;
    }

    /// <summary>Call before each frame's draw pass to set the current context instances.</summary>
    public void BeginFrame(CInstance* self, CInstance* other) {
        _self = self;
        _other = other;
    }

    // --- State ---

    public void SetColor(double color) =>
        Call("draw_set_colour", color);

    public void SetAlpha(double alpha) =>
        Call("draw_set_alpha", alpha);

    // --- Primitives ---

    public void Circle(double x, double y, double radius, bool outline) =>
        Call("draw_circle", x, y, radius, outline ? 1.0 : 0.0);

    public void Rectangle(double x1, double y1, double x2, double y2, bool outline) =>
        Call("draw_rectangle", x1, y1, x2, y2, outline ? 1.0 : 0.0);

    public void Line(double x1, double y1, double x2, double y2) =>
        Call("draw_line", x1, y1, x2, y2);

    public void LineWidth(double x1, double y1, double x2, double y2, double w) =>
        Call("draw_line_width", x1, y1, x2, y2, w);

    public void Triangle(double x1, double y1, double x2, double y2, double x3, double y3, bool outline) =>
        Call("draw_triangle", x1, y1, x2, y2, x3, y3, outline ? 1.0 : 0.0);

    // --- Primitives (vertex-based, for arcs) ---

    public void PrimitiveBegin(PrimitiveKind kind) =>
        Call("draw_primitive_begin", (double)kind);

    public void Vertex(double x, double y) =>
        Call("draw_vertex", x, y);

    public void VertexColor(double x, double y, double color, double alpha) =>
        Call("draw_vertex_colour", x, y, color, alpha);

    public void PrimitiveEnd() =>
        Call("draw_primitive_end");

    // --- Helpers ---

    private void Call(string func, params double[] args) {
        var rv = new RValue[args.Length];
        for (int i = 0; i < args.Length; i++) {
            rv[i] = RV.Real(args[i]);
        }
        _rns.ExecuteCodeFunction(func, _self, _other, rv);
    }

    /// <summary>Construct a GM BGR color from RGB components (0-255 each).</summary>
    public static double ColorRGB(int r, int g, int b) =>
        b * 65536.0 + g * 256.0 + r;
}

public enum PrimitiveKind {
    PointList = 1,
    LineList = 2,
    LineStrip = 3,
    TriangleList = 4,
    TriangleStrip = 5,
    TriangleFan = 6,
}

/// <summary>RValue construction helpers.</summary>
public static class RV {
    public static RValue Real(double v) {
        var r = new RValue();
        r.Type = RValueType.Real;
        r.Real = v;
        return r;
    }
}

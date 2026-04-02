namespace RNSReloaded.CooldownShapes.Shapes;

public static class ShapeFactory {
    private static readonly Dictionary<ShapeType, IShapeRenderer> Renderers = new() {
        { ShapeType.Ring, new RingShape() },
        { ShapeType.Cross, new CrossShape() },
        { ShapeType.X, new XShape() },
        { ShapeType.DiamondGrid, new DiamondGridShape() },
        { ShapeType.DotArray, new DotArrayShape() },
    };

    public static IShapeRenderer Get(ShapeType type) =>
        Renderers.TryGetValue(type, out var r) ? r : Renderers[ShapeType.Ring];
}

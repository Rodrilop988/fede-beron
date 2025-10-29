class ServicioVentas:
    """Responsable de las operaciones de venta."""

    def __init__(self, inventario):
        self.inventario = inventario

    def vender(self, nombre_producto):
        for p in self.inventario:
            if p.get_nombre().lower() == nombre_producto.lower():
                self.inventario.remove(p)
                print(f"✅ Vendido: {p.get_nombre()} por ${p.get_precio():.2f}")
                return
        print("❌ Producto no encontrado.")

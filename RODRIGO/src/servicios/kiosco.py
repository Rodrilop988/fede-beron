class Kiosco:
    """Responsable solo del inventario."""
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.inventario = []

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def mostrar_productos(self):
        print(f"\n🛒 Productos del kiosco {self.nombre}:")
        for p in self.inventario:
            print(" -", p.mostrar_info())


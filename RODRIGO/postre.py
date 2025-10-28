from models.producto import Producto

class Postre(Producto):
    def __init__(self, nombre: str, precio: float, tiene_crema: bool):
        super().__init__(nombre, precio)
        self.tiene_crema = tiene_crema

    def mostrar_info(self):
        tipo = "con crema" if self.tiene_crema else "sin crema"
        return f"Postre: {self._nombre} - ${self._precio:.2f} ({tipo})"

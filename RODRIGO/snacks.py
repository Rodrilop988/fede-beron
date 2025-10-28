from productos import Producto

class Snack(Producto):
    def __init__(self, nombre: str, precio: float, es_salado: bool):
        super().__init__(nombre, precio)
        self.es_salado = es_salado

    def mostrar_info(self):
        tipo = "salado" if self.es_salado else "dulce"
        return f"Snack: {self._nombre} - ${self._precio:.2f} ({tipo})"

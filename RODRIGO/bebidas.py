from models.producto import Producto

# Herencia
class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, es_alcoholica: bool):
        super().__init__(nombre, precio)
        self.es_alcoholica = es_alcoholica

    # Polimorfismo: cada clase redefine mostrar_info a su manera
    def mostrar_info(self):
        tipo = "alcohólica" if self.es_alcoholica else "sin alcohol"
        return f"Bebida: {self._nombre} - ${self._precio:.2f} ({tipo})"

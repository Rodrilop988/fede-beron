from models.producto import Producto


class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, es_alcoholica: bool):
        super().__init__(nombre, precio)
        self.es_alcoholica = es_alcoholica

    
    def mostrar_info(self):
        tipo = "alcohólica" if self.es_alcoholica else "sin alcohol"
        return f"Bebida: {self._nombre} - ${self._precio:.2f} ({tipo})"

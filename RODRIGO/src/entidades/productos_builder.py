from models.bebida import Bebida
from models.snack import Snack
from models.postre import Postre


class ProductoBuilder:
    def __init__(self):
        self._nombre = None
        self._precio = 0.0
        self._tipo = None
        self._atributo_extra = None

    def set_nombre(self, nombre):
        self._nombre = nombre
        return self  

    def set_precio(self, precio):
        self._precio = precio
        return self

    def set_tipo(self, tipo):
        
        self._tipo = tipo.lower()
        return self

    def set_extra(self, extra):
        
        self._atributo_extra = extra
        return self

    def build(self):
        if self._tipo == "bebida":
            return Bebida(self._nombre, self._precio, self._atributo_extra)
        elif self._tipo == "snack":
            return Snack(self._nombre, self._precio, self._atributo_extra)
        elif self._tipo == "postre":
            return Postre(self._nombre, self._precio, self._atributo_extra)
        else:
            raise ValueError("Tipo de producto no válido o no especificado")

from abc import ABC, abstractmethod


class Producto(ABC):
    def __init__(self, nombre: str, precio: float):
        
        self._nombre = nombre
        self._precio = precio

    
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        if precio >= 0:
            self._precio = precio

    @abstractmethod
    def mostrar_info(self):
        pass

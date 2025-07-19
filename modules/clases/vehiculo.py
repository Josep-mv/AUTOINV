from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, precio, vin):
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._precio = precio
        self._vin = vin
        self._disponible = True

    @abstractmethod
    def mostrar_informacion(self):
        pass

    def esta_disponible(self):
        return self._disponible

    def marcar_como_vendido(self):
        self._disponible = False

    @property
    def vin(self):
        return self._vin

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def año(self):
        return self._año

    @property
    def precio(self):
        return self._precio

    @property
    def disponible(self):
        return self._disponible

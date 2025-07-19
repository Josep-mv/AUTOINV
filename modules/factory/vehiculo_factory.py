# Patron de Diseño: Factory
# Este módulo implementa el patrón Factory, encapsulando la creación de objetos Auto
# para mejorar la mantenibilidad, escalabilidad y desacoplar el código de la lógica de construcción.

from modules.clases.auto import Auto

class VehiculoFactory:
    @staticmethod
    def crear_auto(marca, modelo, año, precio, vin, puertas, combustible, automatico):
        """
        Método Factory que crea una instancia de Auto con los parámetros dados.
        Permite centralizar la lógica de creación y facilita la extensión futura
        para crear otros tipos de vehículos.
        """
        return Auto(marca, modelo, año, precio, vin, puertas, combustible, automatico)

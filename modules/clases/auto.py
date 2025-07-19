# Importa la clase base Vehiculo, de la cual Auto va a heredar
from modules.clases.vehiculo import Vehiculo

# Clase Auto que hereda de la clase abstracta Vehiculo (Herencia).
# Permite reutilizar atributos y métodos comunes como marca, modelo, año, precio y vin.
class Auto(Vehiculo):
    # Constructor que recibe atributos del auto y llama al constructor de la clase base
    def __init__(self, marca, modelo, año, precio, vin, puertas, combustible, automatico):
        super().__init__(marca, modelo, año, precio, vin)
        self._puertas = puertas
        self._combustible = combustible
        self._automatico = automatico      # Booleano: True si es automático, False si es manual

    # Calcula el valor del seguro como el 5% del precio
    def calcular_seguro(self):
        return self.precio * 0.05

    # Calcula la depreciación como el 15% del precio
    def calcular_depreciacion(self):
        return self.precio * 0.15

    # Devuelve el tipo de vehículo (en este caso siempre "Auto")
    def obtener_tipo(self):
        return "Auto"

# Implementación del método abstracto mostrar_informacion() definido en Vehiculo.
# Ejemplo de Polimorfismo: cada subclase define su propia versión de este método.
    def mostrar_informacion(self):
        estado = "Disponible" if self.esta_disponible() else "Vendido"
        return (f"{self.marca} {self.modelo} {self.año} - ${self.precio:.2f} - "
                f"VIN: {self.vin} - {estado} - {self._puertas} puertas - "
                f"{self._combustible} - {'Automático' if self._automatico else 'Manual'}")

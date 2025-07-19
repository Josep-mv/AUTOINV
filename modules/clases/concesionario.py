# modules/clases/concesionario.py

from modules.clases.auto import Auto

# Patrón de Diseño: Singleton
# Esta implementación asegura que solo exista una única instancia de la clase Concesionario
# durante la ejecución del programa, controlando la creación desde __new__.

class Concesionario:
    __instancia = None  # atributo de clase para Singleton

    def __new__(cls, nombre, direccion):
        if cls.__instancia is None:
            cls.__instancia = super(Concesionario, cls).__new__(cls)
            cls.__instancia.__initialized = False
        return cls.__instancia

    def __init__(self, nombre, direccion):
        if not self.__initialized:
            # Esto se ejecuta solo una vez
            self.__nombre = nombre
            self.__direccion = direccion
            self.__vehiculos = []
            self.__clientes = {}
            self.__initialized = True  # asegura que no se vuelva a inicializar

    def agregar_vehiculo(self, vehiculo):
        self.__vehiculos.append(vehiculo)

    def registrar_cliente(self, cliente):
        self.__clientes[cliente.dni] = cliente

    def vender_vehiculo(self, vin, cliente):
        """
        Realiza la venta de un vehículo si está disponible.
        Args:
            vin (str): El número VIN del vehículo a vender.
            cliente (Cliente): El objeto Cliente que realiza la compra.
        Returns:
            bool: True si la venta se realizó con éxito, False en caso contrario.
        """
        for v in self.__vehiculos:
            # Accede al VIN del vehículo usando la propiedad 'vin'
            # que está definida en la clase Vehiculo.
            # No se usa '_Vehiculo__vin' porque 'vin' se definió con un solo guion bajo (_vin)
            # y se expuso a través de un @property.
            if v.esta_disponible() and v.vin == vin:
                v.marcar_como_vendido()
                cliente.agregar_vehiculo(v)
                return True
        return False

    def generar_reportes(self):
        """Genera y muestra reportes de vehículos y clientes."""
        print("\n--- REPORTE DE VEHÍCULOS ---")
        for v in self.__vehiculos:
            print(v.mostrar_informacion())

        print("\n--- REPORTE DE CLIENTES ---")
        for c in self.__clientes.values():
            print(c.mostrar_info())

    def obtener_cliente(self, dni):
        """
        Obtiene un cliente por su DNI.
        Args:
            dni (str): El DNI del cliente.
        Returns:
            Cliente: El objeto Cliente si se encuentra, None en caso contrario.
        """
        return self.__clientes.get(dni)

    def obtener_vehiculos(self):
        """
        Devuelve la lista de todos los vehículos en el concesionario.
        Returns:
            list: Una lista de objetos Vehiculo.
        """
        return self.__vehiculos

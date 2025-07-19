import sqlite3

class DBManager:
    _conexion = None
    _cursor = None

    @staticmethod
    def conectar():
        if DBManager._conexion is None:
            try:
                DBManager._conexion = sqlite3.connect("autoland.db")
                DBManager._cursor = DBManager._conexion.cursor()
                print("✅ Conectado a la base de datos autoland.db")
                DBManager.crear_tablas()
            except sqlite3.Error as e:
                print(f"❌ Error al conectar a la base de datos: {e}")

    @staticmethod
    def crear_tablas():
        try:
            DBManager._cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    dni TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    telefono TEXT,
                    email TEXT
                )
            """)
            DBManager._conexion.commit()
            print("✅ Tabla clientes verificada o creada.")
        except sqlite3.Error as e:
            print(f"❌ Error al crear la tabla: {e}")

    @staticmethod
    def registrar_cliente(cliente):
        try:
            DBManager._cursor.execute("""
                INSERT INTO clientes (dni, nombre, apellido, telefono, email)
                VALUES (?, ?, ?, ?, ?)
            """, (cliente.dni, cliente.nombre, cliente.apellido, cliente.telefono, cliente.email))
            DBManager._conexion.commit()
            print("✅ Cliente registrado en la base de datos.")
        except sqlite3.IntegrityError:
            print("⚠️ El cliente ya está registrado (clave duplicada).")
        except sqlite3.Error as e:
            print(f"❌ Error al registrar cliente: {e}")

    @staticmethod
    def obtener_clientes():
        try:
            DBManager._cursor.execute("SELECT * FROM clientes")
            return DBManager._cursor.fetchall()
        except sqlite3.Error as e:
            print(f"❌ Error al obtener clientes: {e}")
            return []

    @staticmethod
    def cerrar():
        if DBManager._conexion:
            DBManager._conexion.close()
            print("🔒 Conexión cerrada.")

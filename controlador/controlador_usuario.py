from modelo.usuario import Usuario
from modelo.db import conectar
from seguridad.CaDe_Main import CaDeMain
import bcrypt

class Registro:

    def __init__(self):
        print("se ha iniciado el controlador de usuarios correctamente")
        pass

    def mostrar_informacion(self, id, correo, contraseña):
        print(f"id: {id}")
        print(f"correo: {correo}")
        print(f"contrasena: {contraseña}")

    def crear_usuario(self, correo, contraseña):
        conn = None
        cursor = None
        try:
            # Validación básica de entrada, se puede usar cuando no se ingresan datos.
            if not correo or not contraseña:
                print("El correo y la contraseña son obligatorios, por favor ingresarlos a continuacion:")
                return False

            # Generar hash de la contraseña
            salt = bcrypt.gensalt()
            hash_contraseña = bcrypt.hashpw(contraseña.encode("utf-8"), salt)


            conn = conectar()
            cursor = conn.cursor()
            query = "INSERT INTO usuarios (correo, contrasena) VALUES (%s, %s)"
            cursor.execute(query, (correo, hash_contraseña.decode("utf-8")))
            conn.commit()

            print(f"Usuario con correo {correo} creado exitosamente.")
            return True
        #Exception es una clase base en Python que captura cualquier error no específico por ejemplo errores de conexión,sintaxis incorrecta,etc
        #La variable e almacena la información detallada del error que ocurrió
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    def autentificar_usuario(self, correo, contraseña):
        conn = None
        cursor = None
        try:
            conn = conectar()
            cursor = conn.cursor()
            query = "SELECT contraseña FROM usuarios WHERE correo = %s"
            cursor.execute(query, (correo,))
            resultado = cursor.fetchone()
            if resultado is None:
                print("Usuario no encontrado.")
                return False  # Usuario no encontrado

            contraseña_hash = resultado[0]
            if bcrypt.checkpw(contraseña.encode("utf-8"), contraseña_hash.encode("utf-8")):
                print("Autenticación exitosa.")
                return True
            else:
                print("Contraseña incorrecta.")
                return False
        except Exception as e:
            print(f"Error al autenticar usuario: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
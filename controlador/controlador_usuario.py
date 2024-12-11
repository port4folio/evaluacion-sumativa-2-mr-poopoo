from modelo.usuario import Usuario
from modelo.db import conectar
import bcrypt

class Registro:

    def __init__(self):
        print("Se ha iniciado el controlador de usuarios correctamente")
        

    def mostrar_informacion(self, id, correo, contraseña):
        print(f"id: {id}")
        print(f"correo: {correo}")
        print(f"contraseña: {contraseña}")

    def crear_usuario(self, correo, contraseña):
        conn = None
        cursor = None
        try:
            # Validación básica, se puede usar cuando no se ingresan datos.
            if not correo or not contraseña:
                print("El correo y la contraseña son obligatorios, por favor ingresarlos a continuacion:")
                return False

            # Generar hash de la contraseña
            salt = bcrypt.gensalt()
            hash_contraseña = bcrypt.hashpw(contraseña.encode("utf-8"), salt)


            conn = conectar()
            cursor = conn.cursor()
            query = "INSERT INTO usuarios (correo, contraseña) VALUES (%s, %s)"
            cursor.execute(query, (correo, hash_contraseña.decode("utf-8")))
            conn.commit()

            print(f"Usuario con correo {correo} creado exitosamente.")
            return True
        #Exception clase base en Python que captura cualquier error no específico , ejemplo errores de conexión,sintaxis incorrecta,etc
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
            cursor.execute(query, (correo,))  #se reemplaza el %s por el correo del usuario que se pasó a la función.
            resultado = cursor.fetchone()

            if resultado is None:
                print("Usuario no encontrado.")
                return False  # usuario no encontrado

            # recuperar la pass desde la base de datos
            contraseña_hash = resultado[0]

            # isinstance es una funcion que permite saber si una variable pertenece a un tipo determinado, se compara el hash recuperado que si es de tipo bytes, se convierte a texto para poder compararlo bien.
            if isinstance(contraseña_hash, bytes):                
                contraseña_hash = contraseña_hash.decode("utf-8")

            # aqui se verifica la igualdad de contraseña ingresada y con la de bd
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

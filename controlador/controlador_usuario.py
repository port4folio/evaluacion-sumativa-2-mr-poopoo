#from modelo.usuario import Usuario
from modelo.db import conectar
from seguridad.CaDe_Main import CaDeMain
from modelo.printer import printer

class Registro:

    def __init__(self):
        #print("se ha iniciado el controlador de usuarios correctamente")
        printer(tipo=0,argumento="Se ha inicializado el controlador de usuarios.")

    def mostrar_informacion(self, id, correo, contraseña):
        #print(f"id: {id}")
        #print(f"correo: {correo}")
        #print(f"contrasena: {contraseña}")
        pass
        
    def crear_usuario(self, correo, contraseña = str):
        conn = None
        cursor = None
        try:
            # Validación básica de entrada, se puede usar cuando no se ingresan datos.
            if not correo or not contraseña:
                #print("El correo y la contraseña son obligatorios, por favor ingresarlos a continuacion:")
                printer(tipo=2,argumento="El correo y la contraseña son obligatorios.")
                return False

            # Generar hash de la contraseña
            hash_contraseña = CaDeMain(contraseña)

            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (correo, contrasena) VALUES (%(correo)s, %(contrasena)s)", {'correo': correo, 'contrasena': hash_contraseña})
            conn.commit()

            #print(f"Usuario con correo {correo} creado exitosamente.")
            printer(tipo=0,argumento="Usuario con correo " + str(correo) + " creado exitosamente.")
            return True
        #Exception es una clase base en Python que captura cualquier error no específico por ejemplo errores de conexión,sintaxis incorrecta,etc
        #La variable e almacena la información detallada del error que ocurrió
        except Exception as e:
            #print(f"Error al crear usuario: {e}")
            printer(tipo=2,argumento="Error al crear usuario. Código de error: \n" + str(e))
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
            cursor.execute("SELECT contrasena FROM usuarios WHERE correo = %(correo)s", {'correo': correo})
            resultado = cursor.fetchone()
            if resultado is None:
                #print("Usuario no encontrado.")
                printer(tipo=1, argumento="Usuario no encontrado.")
                return False  # Usuario no encontrado

            contraseña_hash = resultado[0]
            if (CaDeMain(contraseña) == contraseña_hash):
                #print("Autenticación exitosa.")
                printer(tipo=0,argumento="Autenticación exitosa.")
                return True
            else:
                #print("Contraseña incorrecta.")
                printer(tipo=1,argumento="Contraseña incorrecta.")
                return False
        except Exception as e:
            #print(f"Error al autenticar usuario: {e}")
            printer(tipo=2,argumento="Error al autenticar usuario. Código de error: \n" + str(e))
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
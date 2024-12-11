#from modelo.usuario import Usuario
from modelo.db import conectar
from seguridad.CaDe_Main import GetJson
from modelo.printer import printer
from email_validator import validate_email, EmailNotValidError
from seguridad.check_contraseña import Validar

def mostrar_informacion(print_info = True):
    #print(f"id: {id}")
    #print(f"correo: {correo}")
    #print(f"contrasena: {contraseña}")
    conn = None
    cursor = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, is_admin FROM usuarios")
        usuarios = cursor.fetchall()
        if len(usuarios) > 0:
            cuentas = 0
            printer()
            printer([
                ["-- Usuarios registrados --", None, None]
            ])
            for usuario in usuarios:
                cuentas += 1
                nombre = usuario[0]
                is_admin = usuario[1]
                es_administrador = ""
                match(is_admin):
                    case 0:
                        es_administrador = "No."
                    case 1:
                        es_administrador = "Sí."
                    case _:
                        es_administrador = "No (?)"
                printer([
                    ["----------------", None, None],
                    ["Nombre: " + nombre, None, None],
                    ["Es administrador?: " + es_administrador, None, None],
                    ["", None, None]
                ])
            printer([
                ["Presione ENTER para continuar...", None, None]
            ])
            if print_info:
                input()
            return cuentas
        else:
            if print_info:
                printer(tipo=1,argumento="No se han encontrado usuarios registrados.")
            return 0
    except Exception as e:
        if print_info:
            printer(tipo=2,argumento="No se han podido obtener registros. Código de error: " + str(e))
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_admin(correo, print_info = False):
    conn = None
    cursor = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT is_admin FROM usuarios WHERE correo = %(correo)s", {'correo': correo})
        resultado = cursor.fetchone()
        if resultado is None:
            if print_info:
                printer(tipo=1,argumento="El usuario no es un administrador o no ha sido encontrado.")
            return False
        is_admin = resultado[0]
        if is_admin == 1:
            #el usuario si es admin
            return True
        else:
            if print_info:
                printer(tipo=1,argumento="El usuario no es un administrador.\nNo hay permisos para realizar esta acción.")
            return False
    except Exception as e:
        if print_info:
            printer(tipo=2,argumento="Error al consultar usuario. Código de error: \n" + str(e))
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    
def crear_usuario(nombre, correo, contraseña):
    conn = None
    cursor = None
    try:
        # Validación básica de entrada, se puede usar cuando no se ingresan datos.
        #print("El correo y la contraseña son obligatorios, por favor ingresarlos a continuacion:")
        if not nombre:
            printer(tipo=2,argumento="El nombre de usuario es obligatorio.")
            return False
        if not correo:
            printer(tipo=2,argumento="El correo es obligatorio.")
            return False
        if not contraseña:
            printer(tipo=2,argumento="La contraseña es obligatoria.")
            return False
        try:
            validate_email(correo,check_deliverability=True)
        except EmailNotValidError as e:
            printer(tipo=2,argumento="El correo no es válido. Código de error: " + str(e))
            return False
        #checkear que la contraseña sea correcta
        if (Validar(contraseña) == False):
            printer(tipo=2,argumento="La contraseña no es válida. Debe contener al menos:\n8 caracteres, 1 mayúscula, 1 número y 1 símbolo especial (?, !, $)")
            return False
        # Generar hash de la contraseña
        hash_contraseña = GetJson(contraseña)
        print(hash_contraseña)
        #conectar
        #si no hay usuarios, hacer el primer usuario un administrador.
        admin = 0
        cuentas = mostrar_informacion(print_info=False)
        if cuentas != None:
            if cuentas == 0:
                admin = 1
            else:
                admin = 0
        else:
            admin = 0
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (is_admin, nombre, correo, contrasena) VALUES (%(is_admin)s, %(nombre)s, %(correo)s, %(contrasena)s)", {'is_admin': admin, 'nombre': nombre, 'correo': correo, 'contrasena': hash_contraseña})
        conn.commit()

        #print(f"Usuario con correo {correo} creado exitosamente.")
        printer(tipo=0,argumento="Usuario con correo " + str(correo) + " creado exitosamente.")
        if admin == 1:
            printer(tipo=1,argumento="Usted ha sido registrado como administrador.\nInicie sesión con su correo y contraseña para administrar la BD.")
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

def autentificar_usuario(correo, contraseña):
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
            return -1 # usuario no encontrado

        contraseña_hash = resultado[0]
        if (GetJson(contraseña) == contraseña_hash):
            #print("Autenticación exitosa.")
            printer(tipo=0,argumento="Autenticación exitosa.")
            if get_admin(correo):
                printer(tipo=1, argumento="Usted ha iniciado sesión como administrador.\nTenga cuidado con las acciones destructivas.")
                return 2 # es admin
            return 1 # es usuario normal
        else:
            #print("Contraseña incorrecta.")
            printer(tipo=1,argumento="Contraseña incorrecta.")
            return -2 # contraseña incorrecta
    except Exception as e:
        #print(f"Error al autenticar usuario: {e}")
        printer(tipo=2,argumento="Error al autenticar usuario. Código de error: \n" + str(e))
        return 0 # error interno
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
from vistas.vista_empleado import main_empleado
from vistas.vista_proyecto import main_proyecto
from vistas.vista_departamento import main_departamento
from vistas.vista_registro_tiempo import main_registro_tiempo
from controlador.controlador_usuario import *

usuario_autenticado = False  # Indicador global de autenticación

def Login():
    global usuario_autenticado  # Indicador de autenticación
    controlador_usuario = Registro()

    while True:
        print("----------------MENÚ DE LOGIN------------------")
        print("1. Registro")
        print("2. Inicio de sesión")
        print("3. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                correo = input("Ingrese su correo: ")
                contrasena = input("Ingrese su contraseña: ")
                if controlador_usuario.crear_usuario(correo, contrasena):
                    print("¡Usuario registrado con éxito!")
                    print("Redirigiendo a INICIO DE SESIÓN...")
                    continue  # regresar al menú de login para iniciar sesión

            elif opcion == 2:
                correo = input("Ingrese su correo: ")
                contrasena = input("Ingrese su contraseña: ")
                if controlador_usuario.autentificar_usuario(correo, contrasena):
                    print("BIENVENIDO, autenticación exitosa")
                    usuario_autenticado = True  # maarcar al usuario como autenticado
                    break  # salir del ciclo de login y pasar al menú principal
                else:
                    print("Credenciales incorrectas, intente nuevamente.")

            elif opcion == 3:
                print("Saliendo del login...")
                return  # salir del programa pero sin acceder al menú principal todavia

            else:
                print("Opción no válida, intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número para seleccionar una opción.")

    if not usuario_autenticado:
        print("Debe iniciar sesión para continuar.")
        return  # Salir si el usuario no está autenticado


def menu_principal():
    while True:
        print("----------------MENÚ PRINCIPAL------------------")
        print("1. Empleados")
        print("2. Proyectos")
        print("3. Departamentos")
        print("4. Registros de tiempo")
        print("0. Salir")
        try:
            op = int(input("Seleccione una opción: "))
            if op == 1:
                main_empleado()
            elif op == 2:
                main_proyecto()
            elif op == 3:
                main_departamento()
            elif op == 4:
                main_registro_tiempo()
            elif op == 0:
                print("Gracias. Saliendo del sistema...")
                break
            else:
                print("Debe seleccionar una opción válida.")
        except ValueError:
            print("Error: Debe ingresar un número para seleccionar una opción.")


# llamada inicial al login
Login()

#  acceder al menú principal solamente si el usuario está autenticado
if usuario_autenticado:
    menu_principal()
else:
    print("Fin del programa. Hasta luego.")

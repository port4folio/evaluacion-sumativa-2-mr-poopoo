from vistas.vista_empleado import main_empleado
#from vistas.vista_proyecto import main_pryecto
#from vistas.vista_departamento import main_departamento
#from vistas.vista_registro_tiempo import main_registro_tiempo
from controlador.controlador_usuario import *
from modelo.printer import printer, clean
def Login():
    controlador_usuario = Registro()

    while True:
        #print("1.Registro")
        #print("2.Inicio de sesion")
        #print("3.salir")
        printer([
            ["1. Registro",
             None, clean()],
            ["2. Inicio de sesión",
             None, None],
            ["3. Salir",
             None, None]
        ])
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                printer()
                correo = input("Ingrese su correo: ")
                contrasena = input("Ingrese su contraseña: ")
                if controlador_usuario.crear_usuario(correo, contrasena):
                        #print("BIENVENIDO!")
                        #print("Redirigiendo a INICIO DE SESIÓN...")
                        printer(tipo=0, argumento="Registro completado.\nUsted será redireccionado al inicio de sesión.")
                        continue

            elif opcion == 2:
                    printer([
                        ["-- Menú Inicio de Sesión --", None, clean()]
                    ])
                    correo = input("Ingrese su correo: ")
                    contrasena = input("Ingrese su contraseña: ")

                    if controlador_usuario.autentificar_usuario (correo, contrasena):
                        #print("BIENVENIDO!, autentificacion exitosa")
                        printer(tipo=0, argumento="Autentificación correcta.")
                        menu_principal()
                        break
                    else:
                        #print("credenciales incorrectas, intente nuevamente")
                        #TODO Meter un número de intentos para el login, evita bruteforce y hace cooldown
                        printer(tipo=1,argumento="Credenciales incorrectas.\nIntente nuevamente, por favor.")


            elif opcion == 3:
                    #print("saliendo del programa. !hasta luego!")
                    printer(tipo=0,argumento="Saliendo del programa, hasta luego!")
                    break
            else:
                #print("Opción no válida, intente nuevamente.")
                printer(tipo=1,argumento="Opción no válida, intente nuevamente.")
        except ValueError:
            #print("Error: Debe ingresar un número para seleccionar una opción.")
            printer(tipo=2,argumento="Debe de ingresar un número para la selección correcta.")

Login()

def menu_principal():
    #print("Informe principal")
    #print("1.- Empleados")
    #print("2.- Proyectos")
    #print("3.- Departamentos")
    #print("4.- Registro de tiempo")
    #print("0.- Salir")
    #print("Seleccione una opción: ")
    printer([
        ["-- Informe Principal --",
         None, clean()],
        ["1. Empleados",
         None, None],
        ["2. Proyectos",
         None, None],
        ["3. Departamentos",
         None, None],
        ["4. Registro de tiempo",
         None, None],
        ["0. Salir",
         None, None],
        ["Seleccione una opción.",
         None, None]
    ])
    op=int(input("Opción: "))
    return op

while True:
    op=menu_principal()
    if op==1:
        main_empleado()
    elif op==2:
        #main_pryecto()
        printer(tipo=1)
    elif op==3:
        printer(tipo=1)
        # main_departamento()
    elif op==4:
        printer(tipo=1)
        # main_registro_tiempo()
    elif op==0:
        #print("Gracias")
        printer(tipo=0,argumento="Gracias!")
        break
    else:
        #print("Debe seleccionar una opción válida")
        printer(tipo=2,argumento="Debe seleccionar una opción válida.")
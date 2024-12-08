from vistas.vista_empleado import main_empleado
#from vistas.vista_proyecto import main_pryecto
#from vistas.vista_departamento import main_departamento
#from vistas.vista_registro_tiempo import main_registro_tiempo
from controlador.controlador_usuario import *

def Login():
    controlador_usuario = Registro()

    while True:
        print("1.Registro")
        print("2.Inicio de sesion")
        print("3.salir")
        try:
            opcion = int(input("seleccione una opcion:"))

            if opcion == 1:
                correo = input("Ingrese su correo: ")
                contrasena = input("Ingrese su contraseña: ")
                if controlador_usuario.crear_usuario(correo, contrasena):
                        print("BIENVENIDO!")
                        print("Redirigiendo a INICIO DE SESIÓN...")
                        continue

            elif opcion == 2:
                    correo = input("Ingrese su correo: ")
                    contrasena = input("Ingrese su contraseña: ")

                    if  controlador_usuario.autentificar_usuario (correo, contrasena):
                        print("BIENVENIDO!, autentificacion exitosa")
                        menu_principal()
                        break
                    else:
                        print("credenciales incorrectas, intente nuevamente")

            elif opcion == 3:
                    print("saliendo del programa. !hasta luego!")
                    break
            else:
                print("Opción no válida, intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número para seleccionar una opción.")

Login()


def menu_principal():
    print("Informe principal")
    print("1.- Empleados")
    print("2.- Proyectos")
    print("3.- Departamentos")
    print("4.- Registro de tiempo")
    print("0.- Salir")
    print("Seleccione una opción: ")
    op=int(input("ingrese una opción: "))
    return op

while True:
    op=menu_principal()
    if op==1:
        main_empleado()
    #elif op==2:
        #main_pryecto()
    #elif op==3:
       # main_departamento()
    #elif op==4:
       # main_registro_tiempo()
   # elif op==0:
        print("Gracias")
        break
    else:
        print("Debe seleccionar una opción válida")
        break
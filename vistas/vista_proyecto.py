from modelo.proyecto import Proyecto
from controlador.controlador_proyecto import agregar_proyecto, buscar_proyecto, actualizar_proyecto, obtener_proyectos, eliminar_proyecto
from modelo.printer import printer, clean
def menu():
    #print("Menu proyecto")
    #print("1. Agregar")
    #print("2. Editar")
    #print("3. Imprimir uno")
    #print("4. Imprimir todos")
    #print("5. Eliminar")
    #print("6. Crear tabla")
    #print("0. Salir")
    printer([
        ["-- Menú Proyecto --", None, clean()],
        ["1. Agregar", None, None],
        ["2. Editar", None, None],
        ["3. Imprimir uno", None, None],
        ["4. Imprimir todos", None, None],
        ["5. Eliminar", None, None],
        ["0. Salir", None, None]
    ])
    op=int(input("Ingrese una opcion: "))
    return op

def add_proyecto():
    printer()
    nombre_proyecto=input("Ingrese nombre: ")
    descripcion_proyecto=input("Ingrese descripción breve del proyecto: ")
    fecha_inicio= input("Ingrese fecha de inicio: ")
    proyecto=Proyecto(nombre_proyecto,descripcion_proyecto,fecha_inicio)
    agregar_proyecto(proyecto)

def search_proyecto():
    printer()
    nombre=input("Ingrese empleado a buscar: ")
    proyecto=buscar_proyecto(nombre)
    return proyecto

def edit_proyecto():
    printer()
    proyecto=search_proyecto()
    if proyecto is not None:
        #print("Menu editar")
        #print("1. Nombre")
        #print("2. Direccion")
        #print("3. Telefono")
        #print("4. Correo")
        #print("0. Salir")
        # qué????
        # lo cambié todo para que sea la vista del proyecto, ya que así se llamaba el archivo.
        # voy a hacer la vista departamento en un ratito más (si es que alcanzo).
        printer([
            ["-- Menú Edición --", None, clean()],
            ["1. Nombre", None, None],
            ["2. Descripción", None, None],
            ["3. Fecha de inicio", None, None],
            #["4. Correo", None, None], ?????
            ["0. Salir", None, None]
        ])
        op=int(input("Seleccione una opcion: "))
        if op==1:
            #print(f"El nombre actual es: {proyecto.getNombre()}")
            printer([
                ["El nombre actual es: " + proyecto.get_nombre_proyecto(), None, clean()]
            ])
            nombre=input("Ingrese nuevo nombre: ")
            proyecto.set_nombre_proyecto(nombre)
        elif op==2:
            #print(f"Su direccion actual es: {proyecto.getDireccion()}")
            printer([
                ["La descripción actual es: " + proyecto.get_descripcion_proyecto(), None, clean()]
            ])
            desc=input("Ingrese nueva descripción: ")
            proyecto.set_descripcion_proyecto(desc)
        elif op==3:
            #print(f"Su Telefono actual es : {proyecto.getTelefono()}")
            printer([
                ["La fecha de inicio es: " + proyecto.get_fecha_inicio(), None, clean()]
            ])
            fec=input("Ingrese nueva fecha:")
            proyecto.set_fecha_inicio(fec)
        elif op==4:
            #print(f"Su correo actual es: {proyecto.getCorreo()}")
            #correo=input("Ingrese nuevo correo: ")
            #proyecto.setCorreo(correo)
            #pero XDDDDD
            pass
        else:
            #print("No se realizaron cambios.")
            printer(tipo=1, argumento="No se realizaron cambios.")
        actualizar_proyecto(proyecto)    
    else:
        #print("proyecto no encontrado")
        printer(tipo=2,argumento="No se ha podido encontrar el proyecto.")
    
def print_proyecto():
    printer()
    proyecto=search_proyecto()
    if proyecto is not None:
        #print(proyecto)
        printer([
            ["Proyecto:\n", None, clean()],
            [proyecto, None, None],
            ["Presiona ENTER para continuar...", None, None]
        ])
        input()
    else:
        #print("proyecto no encontrado")
        printer(tipo=2,argumento="No se ha encontrado el proyecto.")

def print_proyectos():
    printer()
    proyectos=obtener_proyectos()
    if proyectos != None:
        if len(proyectos) > 0:
            printer([
                ["Proyectos:\n",None,clean()]
            ])
            for proyecto in proyectos:
                printer([
                    [proyecto,None,None]
                ])
            printer([
                ["Presiona ENTER para continuar...",None,None]
            ])
            input()
        else:
            #print("No hay proyectos ingresados")
            printer(tipo=1,argumento="No hay proyectos ingresados.")
    else:
        printer(tipo=2,argumento="Ha ocurrido un error al obtener los proyectos.")
def delete_proyecto():
    printer()
    proyecto=search_proyecto()
    if proyecto is not None:
        #print(f"Eliminara al proyecto {proyecto.getNombre()}")
        #print("1.-Si")
        #print("2.-No")
        #print("3.-Salir")
        printer([
            ["Desea eliminar el proyecto \"" + proyecto.get_nombre_proyecto + "\"?", None, clean()],
            ["1. Sí", None, None],
            ["2. No", None, None]
        ])
        resp=int(input("Seleccione una opcion: "))
        if resp==1:
            eliminar_proyecto(proyecto)
        else:
            #print("proyecto no eliminado")
            printer(tipo=1,argumento="El proyecto no ha sido eliminado.")
    else:
        #print("proyecto no encontrado")
        printer(tipo=2,argumento="No se ha podido encontrar el proyecto.")

def main_proyecto(datos):
    op= -1
    while op != 0:
        op=menu()
        if op == 1:
            if datos['is_admin'] == 1:
                add_proyecto()
            else:
                printer(tipo=1,argumento="Usted no está registrado como administrador.\nNo se ha podido realizar la operación.")
        elif op ==2:
            if datos['is_admin'] == 1:
                edit_proyecto()
            else:
                printer(tipo=1,argumento="Usted no está registrado como administrador.\nNo se ha podido realizar la operación.")
        elif op==3:
            print_proyecto()
        elif op==4:
            print_proyectos()
        elif op==5:
            if datos['is_admin'] == 1:
                delete_proyecto()
            else:
                printer(tipo=1,argumento="Usted no está registrado como administrador.\nNo se ha podido realizar la operación.")
        #elif op==9:
        #    crear_tabla()

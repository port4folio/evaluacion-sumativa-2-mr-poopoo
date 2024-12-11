from modelo.proyecto import Proyecto
from controlador.controlador_proyecto import  agregar_proyecto, buscar_proyecto, editar_proyecto, eliminar_proyecto

def menu():
    print("------------Menu proyecto--------------")
    print("1. Agregar Proyecto")
    print("2. Buscar Proyecto")
    print("3. Editar Proyecto")
    print("4. Eliminar Poryecto")
    print("0. Salir")
    op=int(input("Ingrese una opcion: "))
    return op

def add_proyecto():
    nombre_proyecto=input("Ingrese nombre del proyecto: ")
    descripcion_proyecto=input("Ingrese breve descripcion del proyecto: ")
    fecha_inicio= input("Ingrese fecha de inicio del proyecto: ")
    proyecto=Proyecto(nombre_proyecto,descripcion_proyecto,fecha_inicio)
    agregar_proyecto(proyecto)

def search_proyecto():
    nombre=input("Ingrese proyecto a buscar: ")
    proyecto=buscar_proyecto(nombre)
    return proyecto

def edit_proyecto():
    proyecto=search_proyecto()
    if proyecto is not None:
        print("-----------Menu editar--------------")
        print("-1. Nombre del proyecto: ")
        print("-2. Descripcion del proyecto: ")
        print("-3. fecha inicio del proyecto: ")
        print("-0. Salir")
        op=int(input("Seleccione una opcion: "))
        if op==1:
            print(f"El nombre actual del proyecto es: {proyecto.get_nombre_proyecto()}")
            nombre=input("Ingrese nuevo nombre del proyecto: ")
            proyecto.set_nombre_proyecto(nombre)
        elif op==2:
            print(f"La descripcion actual es: {proyecto.get_descripcion_proyecto()}")
            descrip=input("Ingrese nueva direccion")
            proyecto.set_descripcion_proyecto(descrip)
        elif op==3:
            print(f"La fecha de inicio del proyecto actual es : {proyecto.get_fecha_inicio()}")
            fecha_inicio=input("Ingrese nuevo telefono:")
            proyecto.set_fecha_inicio(fecha_inicio)
        else:
            print("No se realizaron cambios.")
        editar_proyecto(proyecto)    
    else:
        print("proyecto no encontrado")
    

def delete_proyecto():
    proyecto=search_proyecto()
    if proyecto is not None:
        print(f"Atención usted eliminará el proyecto {proyecto.get_nombre_proyecto()}, está seguro?")
        print("1.-Si")
        print("2.-No")
        print("3.-Salir")
        resp=int(input("Seleccione una opcion: "))
        if resp==1:
            eliminar_proyecto(proyecto)
            print("Se ha eliminado el proyecto con éxito")
        else:
            print("proyecto no eliminado")
    else:
        print("proyecto no encontrado")


def main_proyecto():
    op= -1 #se ejecuta al menos una vez en bucle
    while op != 0:
        op=menu()
        if op == 1:
            add_proyecto()
        elif op ==2:
            search_proyecto()
        elif op==3:
            edit_proyecto()
        elif op==4:
            delete_proyecto()
       

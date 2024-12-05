from modelo.proyecto import Proyecto
from controlador.controlador_proyecto import agregar_proyecto, crear_tabla, buscar_proyecto, actualizar_proyecto, obtener_proyectos, eliminar_proyecto

def menu():
    print("Menu proyecto")
    print("1. Agregar")
    print("2. Editar")
    print("3. Imprimir uno")
    print("4. Imprimir todos")
    print("5. Eliminar")
    print("6. Crear tabla")
    print("0. Salir")
    op=int(input("Ingrese una opcion: "))
    return op

def add_proyecto():
    nombre_proyecto=input("Ingrese nombre : ")
    descripcion_proyecto=input("Ingrese direccion: ")
    fecha_inicio= input("Ingrese fecha de inicio: ")
    proyecto=Proyecto(nombre_proyecto,descripcion_proyecto,fecha_inicio)
    agregar_proyecto(proyecto)

def search_proyecto():
    nombre=input("Ingrese empelado a buscar: ")
    proyecto=buscar_proyecto(nombre)
    return proyecto

def edit_proyecto():
    proyecto=search_proyecto()
    if proyecto is not None:
        print("Menu editar")
        print("1. Nombre")
        print("2. Direccion")
        print("3. Telefono")
        print("4. Correo")
        print("0. Salir")
        op=int(input("Seleccione una opcion: "))
        if op==1:
            print(f"El nombre actual es: {proyecto.getNombre()}")
            nombre=input("Ingrese nuevo nombre: ")
            proyecto.setNombre(nombre)
        elif op==2:
            print(f"Su direccion actual es: {proyecto.getDireccion()}")
            direc=input("Ingrese nueva direccion")
            proyecto.setDireccion(direc)
        elif op==3:
            print(f"Su Telefono actual es : {proyecto.getTelefono()}")
            tel=input("Ingrese nuevo telefono:")
            proyecto.setTelefono(tel)
        elif op==4:
            print(f"Su correo actual es: {proyecto.getCorreo()}")
            correo=input("Ingrese nuevo correo: ")
            proyecto.setCorreo(correo)
        else:
            print("No se realizaron cambios.")
        actualizar_proyecto(proyecto)    
    else:
        print("proyecto no encontrado")
    
def print_proyecto():
    proyecto=search_proyecto()
    if proyecto is not None:
        print(proyecto)
    else:
        print("proyecto no encontrado")

def print_proyectos():
    proyectos=obtener_proyectos()
    if len(proyectos) > 0:
        for proyecto in proyectos:
            print(proyecto)
    else:
        print("No hay proyectos ingresados")

def delete_proyecto():
    proyecto=search_proyecto()
    if proyecto is not None:
        print(f"Eliminara al proyecto {proyecto.getNombre()}")
        print("1.-Si")
        print("2.-No")
        print("3.-Salir")
        resp=int(input("Seleccione una opcion: "))
        if resp==1:
            eliminar_proyecto(proyecto)
        else:
            print("proyecto no eliminado")
    else:
        print("proyecto no encontrado")


def main_proyecto():
    op= -1
    while op != 0:
        op=menu()
        if op == 1:
            add_proyecto()
        elif op ==2:
            edit_proyecto()
        elif op==3:
            print_proyecto()
        elif op==4:
            print_proyectos()
        elif op==5:
            delete_proyecto()
        elif op==9:
            crear_tabla()

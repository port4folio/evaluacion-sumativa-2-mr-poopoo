from modelo.empleado import Empleado
from controlador.controlador_empleado import agregar_empleado, crear_tabla, buscar_empleado, actualizar_empleado, obtener_empleados, eliminar_empleado

def menu():
    print("Menu empleado")
    print("1. Agregar")
    print("2. Editar")
    print("3. Imprimir uno")
    print("4. Imprimir todos")
    print("5. Eliminar")
    print("6. Crear tabla")
    print("0. Salir")
    op=int(input("Ingrese una opcion: "))
    return op

def add_empleado():
    nombre=input("Ingrese nombre : ")
    direccion=input("Ingrese direccion: ")
    telefono=input("Ingrese telefono: ")
    correo= input("Ingrese correo: ")
    fecha_inicio= input("Ingrese fecha de inicio: ")
    sueldo=input("Ingrese sueldo: ")
    empleado=Empleado(nombre,direccion,telefono,correo,fecha_inicio,sueldo)
    agregar_empleado(empleado)

def search_empleado():
    nombre=input("Ingrese empelado a buscar: ")
    empleado=buscar_empleado(nombre)
    return empleado

def edit_empleado():
    empleado=search_empleado()
    if empleado is not None:
        print("Menu editar")
        print("1. Nombre")
        print("2. Direccion")
        print("3. Telefono")
        print("4. Correo")
        print("0. Salir")
        op=int(input("Seleccione una opcion: "))
        if op==1:
            print(f"El nombre actual es: {empleado.getNombre()}")
            nombre=input("Ingrese nuevo nombre: ")
            empleado.setNombre(nombre)
        elif op==2:
            print(f"Su direccion actual es: {empleado.getDireccion()}")
            direc=input("Ingrese nueva direccion")
            empleado.setDireccion(direc)
        elif op==3:
            print(f"Su Telefono actual es : {empleado.getTelefono()}")
            tel=input("Ingrese nuevo telefono:")
            empleado.setTelefono(tel)
        elif op==4:
            print(f"Su correo actual es: {empleado.getCorreo()}")
            correo=input("Ingrese nuevo correo: ")
            empleado.setCorreo(correo)
        else:
            print("No se realizaron cambios.")
        actualizar_empleado(empleado)    
    else:
        print("Empleado no encontrado")
    
def print_empleado():
    empleado=search_empleado()
    if empleado is not None:
        print(empleado)
    else:
        print("Empleado no encontrado")

def print_empleados():
    empleados=obtener_empleados()
    if len(empleados) > 0:
        for empleado in empleados:
            print(empleado)
    else:
        print("No hay empleados ingresados")

def delete_empleado():
    empleado=search_empleado()
    if empleado is not None:
        print(f"Eliminara al empleado {empleado.getNombre()}")
        print("1.-Si")
        print("2.-No")
        print("3.-Salir")
        resp=int(input("Seleccione una opcion: "))
        if resp==1:
            eliminar_empleado(empleado)
        else:
            print("Empleado no eliminado")
    else:
        print("Empleado no encontrado")


def main_empleado():
    op= -1
    while op != 0:
        op=menu()
        if op == 1:
            add_empleado()
        elif op ==2:
            edit_empleado()
        elif op==3:
            print_empleado()
        elif op==4:
            print_empleados()
        elif op==5:
            delete_empleado()
        elif op==9:
            crear_tabla()



from modelo.empleado import Empleado
from controlador.controlador_empleado import agregar_empleado, buscar_empleado, editar_empleado, obtener_empleados, eliminar_empleado
from datetime import datetime
def menu():
    print("----------------MENÚ EMPLEADO-----------------")
    print("1. Agregar")
    print("2. Editar")
    print("3. Imprimir uno")
    print("4. Imprimir todos")
    print("5. Eliminar")
    print("0. Salir")
    op=int(input("Ingrese una opcion: "))
    return op

def add_empleado():
    nombres=input("Ingrese nombre : ")
    paterno=input("Ingrese apellido paterno: ")
    materno=input("Ingrese apellido materno: ")
    telefono=input("Ingrese telefono: ")
    correo= input("Ingrese correo: ")
    direccion= input("Ingrese direccion: ")
    comuna= input("Ingrese comuna: ")
    fecha_inicio= input("Ingrese fecha de inicio: ")
    sueldo=input("Ingrese sueldo: ")
    empleado=Empleado(nombres, paterno,materno,telefono,correo,direccion,comuna,fecha_inicio,sueldo)
    agregar_empleado(empleado)

def search_empleado():
    nombre=input("Ingrese empelado a buscar: ")
    empleado=buscar_empleado(nombre)
    return empleado

def edit_empleado():
    empleado=search_empleado()
    if empleado is not None:
        print("--------------MENÚ EDITAR---------------")
        print("1. Nombres")
        print("2. Paterno")
        print("3. Materno")
        print("4. Telefono")
        print("5. Correo")
        print("6. Direccion")
        print("7. Comuna")
        print("0. Salir")
        op=int(input("Seleccione una opcion: "))
        if op==1:
            print(f"Sus nombres actuales son: {empleado.getNombres()}")
            nombre=input("Ingrese nuevos nombres: ")
            empleado.setNombres(nombre)
        elif op==2:
            print(f"Su apellido paterno actual es: {empleado.getPterno()}")
            paterno=input("Ingrese nuevo apellido paterno: ")
            empleado.setPaterno(paterno)
        elif op==3:
            print(f"Su apellido materno actual es: {empleado.getMaterno()}")
            materno=input("Ingrese nuevo apellido materno: ")
            empleado.setMaterno(materno)
        elif op==4:
            print(f"Su Telefono actual es : {empleado.getTelefono()}")
            tel=input("Ingrese nuevo telefono:")
            empleado.setTelefono(tel)
        elif op==5:
            print(f"Su correo actual es: {empleado.getCorreo()}")
            correo=input("Ingrese nuevo correo: ")
            empleado.setCorreo(correo)
        elif op==6:
            print(f"Su direccion actual es: {empleado.getDireccion()}")
            direc=input("Ingrese su nueva direccion: ")
            empleado.setDireccion(direc)
        elif op==7:
            print(f"Su comuna actual es: {empleado.getComuna()}")
            comuna=input("Ingrese su nueva comuna: ")
            empleado.setComuna(comuna)
        else:
            print("No se realizaron cambios.")
        editar_empleado(empleado)    
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
            print("Empleado eliminado con éxito")
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
    



from modelo.empleado import Empleado
from controlador.controlador_empleado import agregar_empleado, crear_tabla, buscar_empleado, actualizar_empleado, obtener_empleados, eliminar_empleado
from modelo.printer import printer, clean
def menu():
    #print("Menu empleado")
    #print("1. Agregar")
    #print("2. Editar")
    #print("3. Imprimir uno")
    #print("4. Imprimir todos")
    #print("5. Eliminar")
    #print("6. Crear tabla")
    #print("0. Salir")
    printer([
        ["-- Menú Empleado --", None, clean()],
        ["1. Agregar", None, None],
        ["2. Editar", None, None],
        ["3. Imprimir uno", None, None],
        ["4. Imprimir todos", None, None],
        ["5. Eliminar", None, None],
        ["0. Salir", None, None]
    ])
    op=int(input("Ingrese una opción: "))
    return op

def add_empleado():
    printer()
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
    printer()
    nombre=input("Ingrese empleado a buscar: ")
    empleado=buscar_empleado(nombre)
    return empleado

def edit_empleado():
    printer()
    empleado=search_empleado()
    if empleado is not None:
        #print("Menu editar")
        #print("1. Nombres")
        #print("2. Paterno")
        #print("3. Materno")
        #print("4. Telefono")
        #print("5. Correo")
        #print("6. Direccion")
        #print("7. Comuna")
        #print("0. Salir")
        printer([
            ["-- Menú editar --", None, clean()],
            ["1. Nombres", None, None],
            ["2. Paterno", None, None],
            ["3. Materno", None, None],
            ["4. Teléfono", None, None],
            ["5. Correo", None, None],
            ["6. Dirección", None, None],
            ["7. Comuna", None, None],
            ["0. Salir", None, None]
        ])
        op=int(input("Seleccione una opción: "))
        if op==1:
            printer()
            print(f"Sus nombres actuales son: {empleado.getNombres()}")
            nombre=input("Ingrese nuevos nombres: ")
            empleado.setNombres(nombre)
        elif op==2:
            printer()
            print(f"Su apellido paterno actual es: {empleado.getPterno()}")
            paterno=input("Ingrese nuevo apellido paterno: ")
            empleado.setPaterno(paterno)
        elif op==3:
            printer()
            print(f"Su apellido materno actual es: {empleado.getMaterno()}")
            materno=input("Ingrese nuevo apellido materno: ")
            empleado.setMaterno(materno)
        elif op==4:
            printer()
            print(f"Su Telefono actual es : {empleado.getTelefono()}")
            tel=input("Ingrese nuevo telefono:")
            empleado.setTelefono(tel)
        elif op==5:
            printer()
            print(f"Su correo actual es: {empleado.getCorreo()}")
            correo=input("Ingrese nuevo correo: ")
            empleado.setCorreo(correo)
        elif op==6:
            printer()
            print(f"Su direccion actual es: {empleado.getDireccion()}")
            direc=input("Ingrese su nueva direccion: ")
            empleado.setDireccion(direc)
        elif op==7:
            printer()
            print(f"Su comuna actual es: {empleado.getComuna()}")
            comuna=input("Ingrese su nueva comuna: ")
            empleado.setComuna(comuna)
        else:
            printer(tipo=1,argumento="No se realizaron cambios.")
        actualizar_empleado(empleado)    
    else:
        #print("Empleado no encontrado")
        printer(tipo=2,argumento="Empleado no encontrado.")    
def print_empleado():
    printer()
    empleado=search_empleado()
    if empleado is not None:
        #print(empleado)
        printer([
            ["Empleado:\n",None,clean()],
            [empleado,None,None],
            ["Presiona ENTER para continuar...",None,None]
        ])
    else:
        #print("Empleado no encontrado")
        printer(tipo=2,argumento="Empleado no encontrado.")

def print_empleados():
    printer()
    empleados=obtener_empleados()
    if len(empleados) > 0:
        printer([
            ["Empleados:\n",None,clean()],
        ])
        for empleado in empleados:
            #print(empleado)
            printer([
                [empleado, None,None]
            ])
        printer([
            ["Presiona ENTER para continuar...",None,None]
        ])
    else:
        #print("No hay empleados ingresados")
        printer(tipo=2,argumento="No hay empleados ingresados.")

def delete_empleado():
    printer()
    empleado=search_empleado()
    if empleado is not None:
        #print(f"Eliminara al empleado {empleado.getNombre()}")
        #print("1.-Si")
        #print("2.-No")
        #print("3.-Salir")
        printer([
            ["Desea eliminar al empleado " + empleado.getNombres() + "?",None,clean()],
            ["1. Sí",None,None],
            ["2. No", None,None]
        ])
        resp=int(input("Seleccione una opción: "))
        if resp==1:
            eliminar_empleado(empleado)
        else:
            #print("Empleado no eliminado")
            printer(tipo=1,argumento="El empleado no ha sido eliminado.")
    else:
        #print("Empleado no encontrado")
        printer(tipo=2,argumento="El empleado no ha sido encontrado.")


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



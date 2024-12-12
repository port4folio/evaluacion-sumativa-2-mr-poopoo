from datetime import datetime
from modelo.registro_tiempo import Registro_tiempo
from modelo.empleado import Empleado    #aqui accedi a todos los atributos de los empelados para despues llamar el id
from modelo.proyecto import Proyecto
from controlador.controlador_empleado import buscar_empleado_nombre, buscar_empleado_correo, buscar_empleado_id
from controlador.controlador_proyecto import buscar_proyecto
from controlador.controlador_registro_tiempo import buscar_registro, agregar_entrada, agregar_salida
from modelo.printer import printer, clean

# aqui instacié las clases para que puedan ser llamadas y que esten definidas en el chek o no me funcionaba
#empleado = Empleado#('id','contraseña','nombres', 'paterno', 'materno', 'telefono', 'correo', 'direccion', 'comuna', 'fecha_inicio', 'sueldo')
#proyecto = Proyecto#('nombre_proyecto', 'descripcion_proyecto', 'fecha_inicio')
#registro_tiempo=Registro_tiempo

#from controlador.controlador_registro_tiempo import 

def menu():
    #print("--------Menu Registro diario----------")
    #print("1. Entrada")
    #print("2. Salida")
    #print("0. Salir")
    printer([
        ["-- Menú Registro Diario --", None, clean()],
        ["1. Entrada", None, None],
        ["2. Salida", None, None],
        ["0. Salir", None, None]
    ])
    op=int(input("Ingrese una opcion: "))
    return op

entrada = None

#TODO terminar la logica del checkin

def tiempo_ahora():
    date = datetime.now()
    return f"{date.year} {date.month} {date.day} {date.hour} {date.minute} "

def tiempo_desc(time_str,tipo = None):
    time_desc = str(time_str).split()
    match(tipo):
        case 0:
            return time_desc[0]
        case 1:
            return time_desc[1]
        case 2:
            return time_desc[2]
        case 3:
            return time_desc[3]
        case 4:
            return time_desc[4]
        case _:
            return time_desc[3]

def check_in():
    printer()
    nombre_registrandose=input("Ingrese su nombre: ")
    nombre_proyecto = input("Ingrese el nombre del proyecto: ")
    empleado = buscar_empleado_nombre(nombre_registrandose)
    proyecto = buscar_proyecto(nombre_proyecto)
    if empleado != None:
        entrada = tiempo_ahora()
        date = f"{tiempo_desc(entrada,2)}-{tiempo_desc(entrada,1)}-{tiempo_desc(entrada,0)}"
        hour = f"{tiempo_desc(entrada,3)}:{tiempo_desc(entrada,4)}:00"
        #print(f"Se registró su entrada de fecha {date} a las {hour} horas.")
        registro_tiempo = Registro_tiempo(empleado.getId(),proyecto.getId(),hour,"","","")
        registro_tiempo.setFecha(date)
        agregar_entrada(registro_tiempo)
        return registro_tiempo
    else:
        #print("ID no registrado, vuelva a intentarlo.")
        printer(tipo=2,argumento="Usted no está registrado. Vuelva a intentarlo.")
        return None
    
def calcular_horas_trabajadas(registro_tiempo = Registro_tiempo):
    salida = registro_tiempo.get_hra_salida()
    entrada = registro_tiempo.get_hra_entrada()
    if entrada != None:
        salida_split = str(salida).split(":")
        entrada_split = str(entrada).split(":")
        diferencia = int(salida_split[0]) - int(entrada_split[0])
        horas_trabajadas = diferencia
        return horas_trabajadas

def check_out():
    #empleado_registrandose=input("Ingrese su correo: ")
    #empleado = buscar_empleado_correo(empleado_registrandose)
    printer()
    fecha = input("Ingrese la fecha del check-in (dd-mm-aaaa): ")
    empleado_nombre = input("Ingrese su nombre: ")
    descripcion = input("Describa brevemente lo que ha hecho durante el día: ")
    empleado = buscar_empleado_nombre(empleado_nombre)
    id_empleado = empleado.getId()
    registro = buscar_registro(fecha, id_empleado)
    if registro != None:
        salida = tiempo_ahora()
        date = f"{tiempo_desc(salida,2)}-{tiempo_desc(salida,1)}-{tiempo_desc(salida,0)}"
        hour = f"{tiempo_desc(salida,3)}:{tiempo_desc(salida,4)}:00"
        #print(f"Se registró su salida de fecha {date} a las {hour} horas.")
        registro.set_hra_salida(hour)
        horas = calcular_horas_trabajadas(registro)
        registro.setHrs_trabajadas(horas)
        registro.setDescripcion_tareas(descripcion)
        agregar_salida(registro)
        printer([
            ["Se ha registrado su salida. Fecha: " + date + ", Hora: " + hour, None, clean()],
            ["Presiona ENTER para continuar...",None,None]
        ])
        input()
    else:
        #print("ID no registrado, vuelva a intentarlo.")
        printer(tipo=2,argumento="Usted no está registrado. Vuelva a intentarlo.")

def main_registro_tiempo():
    op= -1
    while op != 0:
        op=menu()
        if op == 1:
            check_in()
        elif op ==2:
            check_out()
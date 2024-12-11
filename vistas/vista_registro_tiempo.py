from datetime import datetime
from modelo.registro_tiempo import Registro_tiempo
from modelo.empleado import Empleado    #aqui accedi a todos los atributos de los empelados para despues llamar el id
from modelo.proyecto import Proyecto
from controlador.controlador_empleado import buscar_empleado
from controlador.controlador_proyecto import buscar_proyecto
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
    empleado = buscar_empleado(nombre_registrandose)
    proyecto = buscar_proyecto(nombre_proyecto)
    if empleado != None:
        entrada = tiempo_ahora()
        date = f"{tiempo_desc(entrada,2)}/{tiempo_desc(entrada,1)}/{tiempo_desc(entrada,0)}"
        hour = f"{tiempo_desc(entrada,3)}:{tiempo_desc(entrada,4)}:00"
        #print(f"Se registró su entrada de fecha {date} a las {hour} horas.")
        registro_tiempo = Registro_tiempo(empleado.get_id(),proyecto.get_id(),date,hour,"","","")
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

def check_out(registro_tiempo = Registro_tiempo):
    empleado_registrandose=input("Ingrese su correo: ")
    empleado = buscar_empleado(empleado_registrandose)
    if empleado != None:
        salida = tiempo_ahora()
        date = f"{tiempo_desc(salida,2)}/{tiempo_desc(salida,1)}/{tiempo_desc(salida,0)}"
        hour = f"{tiempo_desc(salida,3)}:{tiempo_desc(salida,4)}:00"
        #print(f"Se registró su salida de fecha {date} a las {hour} horas.")
        printer([
            ["Se ha registrado su salida. Fecha: " + date + ", Hora: " + hour, None, clean()],
            ["Presiona ENTER para continuar...",None,None]
        ])
        horas = calcular_horas_trabajadas(salida)
        registro_tiempo.setHrs_trabajadas(horas)
        registro_tiempo.set_hra_salida(hour)
        input()
        return registro_tiempo
    else:
        #print("ID no registrado, vuelva a intentarlo.")
        printer(tipo=2,argumento="Usted no está registrado. Vuelva a intentarlo.")
        
def agregar_registro_tiempo(id_empleado = 0, id_proyecto = 0, fecha = "",)

def main_registro_tiempo(datos):
    op= -1
    while op != 0:
        op=menu()
        if op == 1:
            check_in()
        elif op ==2:
            check_out()
        elif op==3:
            if datos['is_admin'] == 1:

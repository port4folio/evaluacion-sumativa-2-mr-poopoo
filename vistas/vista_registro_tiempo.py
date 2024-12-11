from datetime import datetime
from modelo.registro_tiempo import Registro_tiempo
from modelo.empleado import Empleado    #aqui accedi a todos los atributos de los empelados para despues llamar el id
from modelo.proyecto import Proyecto
from controlador.controlador_empleado import buscar_empleado
from modelo.printer import printer, clean

# aqui instacié las clases para que puedan ser llamadas y que esten definidas en el chek o no me funcionaba
empleado = Empleado#('id','contraseña','nombres', 'paterno', 'materno', 'telefono', 'correo', 'direccion', 'comuna', 'fecha_inicio', 'sueldo')
proyecto = Proyecto#('nombre_proyecto', 'descripcion_proyecto', 'fecha_inicio')
registro_tiempo=Registro_tiempo

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

def check_in():
    nombre_registrandose=input("Ingrese su nombre: ")
    empleado = buscar_empleado(nombre_registrandose)
    if id_registrandose == empleado.get_id():
        entrada = datetime.now()
        date = entrada.strftime('%d-%m-%Y')
        hour = entrada.strftime('%H:%M')
        descripcion=input("Describa las actividades del dia: ")
        print(f"Se registró su entrada de fecha {date} a las {hour} horas.")
        Registro_tiempo.set_fecha(date)
        Registro_tiempo.set_hra_entrada(hour)
        Registro_tiempo.set_descripcion_tareas(descripcion)
        Registro_tiempo.set_id_empleado(id_registrandose)
        Registro_tiempo.set_id_proyecto(proyecto.get_id)
    else:
        print("ID no registrado, vuelva a intentarlo.")
    
def check_out():
    id_registrandose=int(input("Ingrese su ID: "))
    if id_registrandose == empleado.get_id():
        salida = datetime.now()
        date = salida.strftime('%d-%m-%Y')
        hour = salida.strftime('%H:%M')
        print(f"Se registró su salida de fecha {date} a las {hour} horas.")
        calcular_horas_trabajadas(salida)
        Registro_tiempo.set_hra_salida(hour)
    else:
        print("ID no registrado, vuelva a intentarlo.")
    
def calcular_horas_trabajadas(salida):
    if entrada:
        diferencia = salida - entrada
        horas_trabajadas = diferencia.total_seconds() / 3600
        Registro_tiempo.set_hrs_trabajadas(horas_trabajadas)
        
def main_registro_tiempo():
    op= -1
    while op != 0:
        op=menu()
        if op == 1:
            check_in()
        elif op ==2:
            check_out()

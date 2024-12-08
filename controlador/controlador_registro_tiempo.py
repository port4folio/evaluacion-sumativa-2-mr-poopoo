from modelo.db import conectar
from modelo.registro_tiempo import Registro_tiempo

def agregar_entrada(Registro_tiempo):
    conn = conectar()
    cursor = None
    try:
        if conn is not None:
            cursor = conn.cursor()  
            # Insert Tabla Registro_tiempo
            cursor.execute(
                "INSERT INTO registro_tiempo (fecha,id_empleado,id_proyecto,hra_entrada,descripcion_tareas) VALUES (%s, %s, %s, %s, %s)", (
                    Registro_tiempo.get_fecha(), Registro_tiempo.get_id_empleado(), Registro_tiempo.get_id_proyecto(), Registro_tiempo.get_hra_entrada(),Registro_tiempo.get_descripcion_tareas()
                )
            )
            conn.commit()
            print("Entrada ingresada")
    except Exception as e:
        print(f"No se agregaron registros {e}")
    finally:

        if cursor:
            cursor.close()
        
        if conn:
            conn.close()
            
def agregar_salida(Registro_tiempo):
    conn = conectar()
    cursor = None
    try:
        if conn is not None:
            cursor = conn.cursor()  
            # Insert Tabla Registro_tiempo
            cursor.execute(
                "INSERT INTO registro_tiempo (hra_salida,hrs_trabajadas) VALUES (%s, %s)", (
                    Registro_tiempo.get_hra_salida(),Registro_tiempo.get_hrs_trabajadas()
                )
            )
            conn.commit()
            print("Salida ingresada")
    except Exception as e:
        print(f"No se agregaron registros {e}")
    finally:

        if cursor:
            cursor.close()
        
        if conn:
            conn.close()
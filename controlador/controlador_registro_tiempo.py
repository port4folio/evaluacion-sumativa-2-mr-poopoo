from modelo.db import conectar
from modelo.registro_tiempo import Registro_tiempo
from modelo.printer import printer

#def agregar_registro_tiempo()

def agregar_entrada(registro_tiempo = Registro_tiempo):
    printer()
    conn = conectar()
    cursor = None
    try:
        if conn is not None:
            cursor = conn.cursor()  
            # Insert Tabla Registro_tiempo
            cursor.execute(
                "INSERT INTO registro_tiempo (fecha,id_empleado,id_proyecto,hra_entrada,descripcion_tareas) VALUES (%s, %s, %s, %s, %s)", (
                    registro_tiempo.getFecha(), registro_tiempo.getId_empleado(), registro_tiempo.getId_proyecto(), registro_tiempo.get_hra_entrada(),registro_tiempo.getDescripcion_tareas()
                )
            )
            conn.commit()
            #print("Entrada ingresada")
            printer(tipo=0,argumento="Entrada ingresada correctamente.")
            #TODO continuar reemplazando prints
    except Exception as e:
        #print(f"No se agregaron registros {e}")
        printer(tipo=2,argumento="No se agregaron registros. Código de error: " + str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            
def agregar_salida(registro_tiempo=Registro_tiempo):
    printer()
    conn = conectar()
    cursor = None
    try:
        if conn is not None:
            cursor = conn.cursor()  
            # Insert Tabla Registro_tiempo
            cursor.execute(
                "UPDATE registro_tiempo SET hra_salida = %s, hrs_trabajadas = %s WHERE fecha = %s AND id_empleado = %s", (
                    registro_tiempo.get_hra_salida(),registro_tiempo.get_hrs_trabajadas(), registro_tiempo.getFecha(), registro_tiempo.getId_empleado()
                )
            )
            conn.commit()
            #print("Salida ingresada")
            printer(tipo=0,argumento="Salida ingresada correctamente.")
    except Exception as e:
        #print(f"No se agregaron registros {e}")
        printer(tipo=2,argumento="No se agregaron registros. Código de error: " + str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def buscar_registro(fecha, id_empleado):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor(buffered=True)
            # Select Tabla proyecto
            cursor.execute(
                "SELECT fecha,id_empleado,id_proyecto,hra_entrada,descripcion_tareas FROM registro_tiempo WHERE fecha=%(fecha)s AND id_empleado=%(id_empleado)s",
                {'fecha': fecha, 'id_empleado': id_empleado}
                )
            registro=cursor.fetchone()
            if registro is not None:
                registro_encontrado=Registro_tiempo(registro[2],registro[3],registro[4])
                registro_encontrado.setFecha(registro[0])
                registro_encontrado.setId_empleado(registro[1])
            else:
                registro_encontrado=None
            return registro_encontrado
        else:
            return None
    except Exception as e:
        #print(f"Error al conectar. {e}")
        printer(tipo=2,argumento="No se ha podido obtener el registro. Código de error:\n" + str(e))
    finally:
        cursor.close()
        conn.close()
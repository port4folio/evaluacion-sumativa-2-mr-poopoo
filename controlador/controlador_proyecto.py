from modelo.db import conectar
from modelo.proyecto import Proyecto
from modelo.printer import printer
def agregar_proyecto(proyecto = Proyecto):
    conn = conectar()
    cursor = None
    try:
        if conn is not None:
            cursor = conn.cursor()
            # Insert Tabla Proyecto
            cursor.execute(
                "INSERT INTO proyecto (nombre_proyecto,descripcion_proyecto,fecha_inicio) VALUES (%s, %s, %s)", (proyecto.get_nombre_proyecto(), proyecto.get_descripcion_proyecto(), proyecto.get_fecha_inicio()))
            conn.commit()
            #print("Proyecto ingresado")
            printer(tipo=0,argumento="Proyecto ingresado correctamente.")
    except Exception as e:
        #print(f"No se agregaron registros {e}")
        printer(tipo=2,argumento="No se han ingresado registros. Código de error:\n" + str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def actualizar_proyecto(proyecto = Proyecto):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            # Update Tabla Proyecto
            cursor.execute("UPDATE proyecto SET nombre_proyecto=%s,descripcion_proyecto=%s,fecha_inicio=%s WHERE id_proyecto=%s", (proyecto.get_nombre_proyecto(),proyecto.get_descripcion_proyecto(),proyecto.get_fecha_inicio(), proyecto.get_id()))
            conn.commit()
            #print("Proyecto actualizado")
            printer(tipo=0,argumento="Proyecto actualizado.")
    except Exception as e:
        #print(f"No se agregaron registros {e}")
        printer(tipo=2,argumento="No se actualizaron registros. Código de error: \n" + str(e))
    finally:
        cursor.close()
        conn.close()

def buscar_proyecto(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor(buffered=True)
            # Select Tabla proyecto
            cursor.execute(
                "SELECT id_proyecto,nombre_proyecto,descripcion_proyecto,fecha_inicio FROM proyecto WHERE nombre_proyecto=%(nombre)s",
                {'nombre': nombre}
                )
            proyecto=cursor.fetchone()
            if proyecto is not None:
                proyecto_encontrado=Proyecto(proyecto[1],proyecto[2],proyecto[3])
                proyecto_encontrado.setId(proyecto[0])
            else:
                proyecto_encontrado=None
            return proyecto_encontrado
        else:
            return None
    except Exception as e:
        #print(f"Error al conectar. {e}")
        printer(tipo=2,argumento="No se ha podido obtener el proyecto. Código de error:\n" + str(e))
    finally:
        cursor.close()
        conn.close()

def obtener_proyectos():
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("SELECT id_proyecto,nombre_proyecto,descripcion_proyecto,fecha_inicio FROM proyecto")
            proyecto_encontrado = cursor.fetchall()
            proyecto_lista = []
            if len(proyecto_encontrado) > 0:
                for proyecto in proyecto_encontrado:
                    proyecto_encontrado=Proyecto(proyecto[1],proyecto[2],proyecto[3])
                    proyecto_encontrado.set_id(proyecto[0])
                    proyecto_lista.append(proyecto_encontrado)
                return proyecto_lista
            else:
                return None
        else:
            return None
    except Exception as e:
        #print(f"Error al conectar. {e}")
        printer(tipo=2,argumento="Error al obtener. Código de error:\n" + str(e))
    finally:
        cursor.close()
        conn.close()

def eliminar_proyecto(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM proyecto WHERE nombre_proyecto = %s",(nombre))
            conn.commit()
            #print("Proyecto eliminado")
            printer(tipo=0,argumento="Proyecto eliminado correctamente.")
    except Exception as e:
        #print(f"No se eliminaron registros {e}")
        printer(tipo=2,argumento="No se eliminaron registros. Código de error:\n" + str(e))
    finally:
        cursor.close()
        conn.close()
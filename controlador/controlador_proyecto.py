from modelo.db import conectar
from modelo.proyecto import Proyecto

def agregar_proyecto(proyecto):
    conn = conectar()
    cursor = None
    try:
        if conn is not None:
            cursor = conn.cursor()  
            # Insert Tabla Proyecto
            cursor.execute(
                "INSERT INTO proyecto (nombre_proyecto,descripcion_proyecto,fecha_inicio) VALUES (%s, %s, %s)", (
                    proyecto.getNombre_proyecto(), proyecto.getDescripcion_proyecto(), proyecto.getFecha_inicio()
                )
            )
            conn.commit()
            print("Proyecto ingresado")
    except Exception as e:
        print(f"No se agregaron registros {e}")
    finally:

        if cursor:
            cursor.close()
        
        if conn:
            conn.close()

def buscar_proyecto(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            # Select Tabla proyecto
            cursor.execute(
                "SELECT id,nombre,descripcion,gerente FROM proyecto WHERE nombre=%s",
                (nombre)
                )
            proyecto=cursor.fetchone()
            if proyecto is not None:
                proyecto_encontrado=Proyecto(proyecto[1],proyecto[2],proyecto[3])
                proyecto_encontrado.set_id(proyecto[0])
            else:
                proyecto_encontrado=None
            return proyecto_encontrado
        else:
            return None
    except Exception as e:
        print(f"Error al conectar. {e}")
    finally:
        cursor.close()
        conn.close()

def obtener_proyecto():
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("SELECT id,nombre,descripcion,gerente FROM proyecto")
            proyecto_encontrado = cursor.fetchall()
            proyecto = []
            if len(proyecto_encontrado) > 0:
                for proyecto in proyecto_encontrado:
                    proyecto_encontrado=Proyecto(proyecto[1],proyecto[2],proyecto[3])
                    proyecto_encontrado.set_id(proyecto[0])
                    proyecto.append(proyecto_encontrado)
                return proyecto
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"Error al conectar. {e}")
    finally:
        cursor.close()
        conn.close()

def editar_proyecto(proyecto):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            # Update Tabla Empleado
            cursor.execute("UPDATE proyecto SET nombre_proyecto=%s, descripcion_proyecto=%s, fecha_inicio=%s",
                        (proyecto.getNombre_proyecto(), proyecto.getDescripcion_proyecto(), proyecto.getFecha_inicio())
            )
            conn.commit()
            print("Empleado actualizado")
    except Exception as e:
        print(f"No se agregaron registros {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_proyecto(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM proyecto WHERE nombre = %s",(nombre))
            conn.commit()
            print("Proyecto eliminado")
    except Exception as e:
        print(f"No se eliminaron registros {e}")
    finally:
        cursor.close()
        conn.close()
from modelo.db import conectar
from modelo.empleado import Empleado
from modelo.printer import printer
def agregar_empleado(empleado = Empleado):
    conn = conectar()
    cursor = None
    try:
        if conn is not None:
            cursor = conn.cursor()  
            # Insert Tabla Empleados
            cursor.execute(
                "INSERT INTO empleado (nombres, paterno, materno, telefono, correo, direccion, comuna, fecha_inicio, sueldo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (empleado.getNombres(), empleado.getPaterno(), empleado.getMaterno(),empleado.getTelefono(), empleado.getCorreo(), empleado.getDireccion(), 
                 empleado.getComuna(), empleado.getFecha_inicio(), empleado.getSueldo())
            )
            conn.commit()
            #print("Empleado ingresado")
            printer(tipo=0,argumento="Empleado ingresado correctamente.")
    except Exception as e:
        #print(f"No se agregaron registros {e}")
        printer(tipo=2,argumento="No se agregaron registros. Código de error:\n" + str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def actualizar_empleado(empleado = Empleado):
    conn=conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            # Update Tabla Empleado
            cursor.execute("UPDATE empleado SET nombres=%s, paterno=%s, materno=%s, telefono=%s, correo=%s, direccion=%s, comuna=%s, fecha_inicio=%s, sueldo=%s WHERE id_empleado=%s",
                        (empleado.getNombres(), empleado.getPaterno(), empleado.getMaterno(),empleado.getTelefono(), empleado.getCorreo(), empleado.getDireccion(), 
                 empleado.getComuna(), empleado.get_fecha_inicio(), empleado.get_sueldo(), empleado.get_id())
            )
            conn.commit()
            #print("Empleado actualizado")
            printer(tipo=0,argumento="Empleado añadido correctamente.")
    except Exception as e:
        #print(f"No se agregaron registros {e}")
        printer(tipo=2,argumento="No se actualizaron registros. Código de error:\n" + str(e))
    finally:
        cursor.close()
        conn.close()


def buscar_empleado(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            # Select Tabla Empleados
            cursor.execute(
                "SELECT id_empleado, nombres, paterno, materno, telefono, correo,direccion, comuna, fecha_inicio,sueldo FROM empleado WHERE nombres=%(nombre)s",
                {'nombre': nombre}
                )
            empleado=cursor.fetchone()
            if empleado != None:
                empleado_encontrado=Empleado(
                    empleado[1],
                    empleado[2],
                    empleado[3],
                    empleado[4],
                    empleado[5],
                    empleado[6],
                    empleado[7],
                    empleado[8],
                    empleado[9]
                )
                empleado_encontrado.set_id(empleado[0])
            else:
                empleado_encontrado=None
            return empleado_encontrado
        else:
            return None
    except Exception as e:
        #print(f"Error al conectar. {e}")
        printer(tipo=2,argumento="No se pudo obtener información. Código de error:\n" + str(e))
    finally:
        cursor.close()
        conn.close()

    
def obtener_empleados():
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("SELECT id_empleado,nombres,paterno,materno,telefono,correo,direccion,comuna,fecha_inicio,sueldo FROM empleado")
            empleados_encontrados = cursor.fetchall()
            empleados_lista = []
            if len(empleados_encontrados) > 0:
                for empleado in empleados_encontrados:
                    empleado_encontrado=Empleado(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[9])
                    empleado_encontrado.set_id(empleado[0])
                    empleados_lista.append(empleado_encontrado)
                return empleados_lista
            else:
                return None
        else:
            return None
    except Exception as e:
        #print(f"Error al conectar. {e}")
        printer(tipo=2,argumento="No se pudo obtener información. Código de error:\n" + str(e))
    finally:
        cursor.close()
        conn.close()
    
def eliminar_empleado(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM empleado WHERE nombres = %s",{nombre})
            conn.commit()
            #print("Empleado eliminado")
            printer(tipo=0, argumento="Empleado eliminado correctamente.")
    except Exception as e:
        #print(f"No se eliminaron registros {e}")
        printer(tipo=2,argumento="No se eliminaron registros. Código de error:\n" + str(e))
    finally:
        cursor.close()
        conn.close()
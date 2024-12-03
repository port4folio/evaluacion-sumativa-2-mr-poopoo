from modelo.db import conectar
from modelo.empleado import Empleado
def agregar_empleado(empleado):
    conn = conectar()
    cursor = None
    try:
        if conn is not None:
            cursor = conn.cursor()  
            # Insert Tabla Empleados
            cursor.execute(
                "INSERT INTO empleado (nombre, direccion, telefono, correo, fecha_inicio, sueldo) VALUES (%s, %s, %s, %s, %s, %s)",
                (empleado.getNombre(), empleado.getDireccion(), empleado.getTelefono(), 
                 empleado.getCorreo(), empleado.get_fecha_inicio(), empleado.get_sueldo())
            )
            conn.commit()
            print("Empleado ingresado")
    except Exception as e:
        print(f"No se agregaron registros {e}")
    finally:
       
        if cursor:
            cursor.close()
        
        if conn:
            conn.close()

def actualizar_empleado(empleado):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            # Update Tabla Empleado
            cursor.execute("UPDATE empleado SET nombre=%s,direccion=%s,telefono=%s, correo=%s, fecha_inicio=%s, sueldo=%s WHERE id=%s",
                        (empleado.getNombre(),empleado.getDireccion(),empleado.getTelefono(),empleado.getCorreo(), empleado.get_fecha_inicio(), empleado.get_sueldo(), empleado.get_id()))
            conn.commit()
            print("Empleado actualizado")
    except Exception as e:
        print(f"No se agregaron registros {e}")
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
                "SELECT id,nombre,direccion,telefono,correo,fecha_inicio,sueldo FROM empleado WHERE nombre=%s",
                (nombre,)
                )
            empleado=cursor.fetchone()
            if empleado is not None:
                empleado_encontrado=Empleado(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6])
                empleado_encontrado.set_id(empleado[0])
            else:
                empleado_encontrado=None
            return empleado_encontrado
        else:
            return None
    except Exception as e:
        print(f"Error al conectar. {e}")
    finally:
        cursor.close()
        conn.close()

# def crear_tabla():#Función para crear las tablas en la base de datos
# conn = conectar()
# if conn is None:
# return
# cursor = conn.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS empleado (
# id INT AUTO_INCREMENT PRIMARY KEY,
# nombre VARCHAR(255) NOT NULL,
# direccion VARCHAR(255) NOT NULL,
# telefono VARCHAR(20) NOT NULL,
# correo VARCHAR(255) NOT NULL,
# fecha_inicio DATE NOT NULL,
# sueldo FLOAT NOT NULL
# )
# ''')
# conn.commit()
# cursor.close()
# conn.close() 
    
def obtener_empleados():
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("SELECT id,nombre,direccion,telefono,correo,fecha_inicio,sueldo FROM empleado")
            empleados_encontrados = cursor.fetchall()
            empleados = []
            if len(empleados_encontrados) > 0:
                for empleado in empleados_encontrados:
                    empleado_encontrado=Empleado(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6])
                    empleado_encontrado.set_id(empleado[0])
                    empleados.append(empleado_encontrado)
                return empleados
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"Error al conectar. {e}")
    finally:
        cursor.close()
        conn.close()
    
def eliminar_empleado(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM empleado WHERE nombre = %s",(nombre))
            conn.commit()
            print("Empleado eliminado")
    except Exception as e:
        print(f"No se eliminaron registros {e}")
    finally:
        cursor.close()
        conn.close()
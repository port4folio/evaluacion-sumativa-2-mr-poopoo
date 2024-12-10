from modelo.db import conectar
from modelo.departamento import Departamento
from modelo.printer import printer
def agregar_departamento(departamento = Departamento):
    conn = conectar()
    cursor = None
    try:
        if conn is not None:
            cursor = conn.cursor()  
            # Insert Tabla Departamento
            cursor.execute(
                "INSERT INTO departamento (nombre,descripcion,gerente) VALUES (%s, %s, %s)", (
                    departamento.get_nombre(), departamento.get_descripcion(), departamento.get_gerente()
                )
            )
            conn.commit()
            #print("Departamento ingresado")
            printer(tipo=0,argumento="Departamento ingresado correctamente.")
            #TODO seguir con este controlador
    except Exception as e:
        #print(f"No se agregaron registros {e}")
        printer(tipo=2,argumento="No se agregaron registros. Código de error:\n" + str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def actualizar_departamento(departamento = Departamento):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            # Update Tabla Departamento
            cursor.execute("UPDATE departamento SET nombre=%s,descripcion=%s,gerente=%s WHERE id_departamento=%s",
                        (departamento.get_nombre(),departamento.get_descripcion(),departamento.get_gerente(), departamento.get_id_departamento()))
            conn.commit()
            #print("Departamento actualizado")
            printer(tipo=0,argumento="Departamento actualizado correctamente.")
    except Exception as e:
        #print(f"No se agregaron registros {e}")
        printer(tipo=2,argumento="No se actualizaron registros. Código de error:\n" + str(e))
    finally:
        cursor.close()
        conn.close()

def buscar_departamento(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            # Select Tabla Departamento
            cursor.execute(
                "SELECT id_departamento,nombre,descripcion,gerente FROM departamento WHERE nombre=%s",
                (nombre)
                )
            departamento=cursor.fetchone()
            if departamento is not None:
                departamento_encontrado=Departamento(departamento[1],departamento[2],departamento[3])
                departamento_encontrado.set_id_departamento(departamento[0])
            else:
                departamento_encontrado=None
            return departamento_encontrado
        else:
            return None
    except Exception as e:
        #print(f"Error al conectar. {e}")
        printer(tipo=2,argumento="No se obtuvieron registros. Código de error:\n" + str(e))
    finally:
        cursor.close()
        conn.close()

def obtener_departamentos():
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("SELECT id_departamento,nombre,descripcion,gerente FROM departamento")
            departamentos_encontrados = cursor.fetchall()
            departamento_lista = []
            if len(departamento_encontrado) > 0:
                for departamento in departamentos_encontrados:
                    departamento_encontrado=Departamento(departamento[1],departamento[2],departamento[3])
                    departamento_encontrado.set_id_departamento(departamento[0])
                    departamento_lista.append(departamento_encontrado)
                return departamento_lista
            else:
                return None
        else:
            return None
    except Exception as e:
        #print(f"Error al conectar. {e}")
        printer(tipo=2,argumento="No se obtuvieron registros. Código de error:\n" + str(e))
    finally:
        cursor.close()
        conn.close()

def eliminar_departamento(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM departamento WHERE nombre = %s",(nombre))
            conn.commit()
            #print("Departamento eliminado")
            printer(tipo=0,argumento="Departamento eliminado correctamente.")
    except Exception as e:
        #print(f"No se eliminaron registros {e}")
        printer(tipo=2,argumento="No se eliminaron registros. Código de error:\n" + str(e))
    finally:
        cursor.close()
        conn.close()
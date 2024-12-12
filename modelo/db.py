# librería para conectar con la base de datos
# pip install mysql-connector-python
# Para crear un archivo con el listado de librerías de mi proyecto
# pip freeze > requeriments.txt

#TODO crear una database en pythonanywhere y usar todo ahí para no instalar XAMPP en todo dispositivo
from modelo.printer import printer

import mysql.connector
from mysql.connector import Error

def conectar():
  try:
    conn = mysql.connector.connect(
      host = 'localhost',
      database = 'db_empleados',
      #database = 'db_final',
      user = 'admin_empleados',
      password = '12345678'
    )
    return conn
  except Error as e:
    #print(f'No se pudo conectar {e}')
    printer(tipo=2,argumento="No se pudo conectar. Razón: " + str(e))
    return None
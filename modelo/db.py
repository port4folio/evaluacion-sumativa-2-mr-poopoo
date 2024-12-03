# librería para conectar con la base de datos
# pip install mysql-connector-python
# Para crear un archivo con el listado de librerías de mi proyecto
# pip freeze > requeriments.txt

import mysql.connector
from mysql.connector import Error

def conectar():
  try:
    conn = mysql.connector.connect(
      host = 'localhost',
      database = 'bdvpoos',
      user = 'dbuservpoos', 
      password = '12345678'
    )
    return conn
  except Error as e:
    print(f'No se pudo conectar {e}')
    return None
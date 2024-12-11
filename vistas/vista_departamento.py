from modelo.departamento import Departamento
from modelo.printer import printer
from controlador.controlador_departamento import agregar_departamento, buscar_departamento, actualizar_departamento, obtener_departamentos, eliminar_departamento

def menu_departamento():
  #print('-----------Menu Departamento-----------')
  #print("1.- Agregar")
  #print("2.- Editar")
  #print("3.- Imprimir una")
  #print("4.- Imprimir todas")
  #print("5.- Eliminar")
  #print("0.- Salir")
  printer()
  printer([
    ["-- Menú Departamento --", None, None],
    ["1. Agregar", None, None],
    ["2. Editar", None, None],
    ["3. Imprimir uno", None, None],
    ["4. Imprimir todos", None, None],
    ["5. Eliminar", None, None],
    ["0. Salir", None, None]
  ])
  op = int(input("Ingrese una opción: "))
  return op

def add_departamento():
  printer()
  #print('Ingrese los datos del departamento')
  nombre = input('Ingrese el nombre: ')
  descripcion= input('Ingrese descripcion: ')
  gerente = input('Ingrese el gerente: ')
  departamento = Departamento(nombre, descripcion, gerente)
  agregar_departamento(departamento)

def search_departamento():
  printer()
  nombre = input('Ingrese el nombre del departamento: ')
  departamento = buscar_departamento(nombre)
  return departamento

def edit_departamento():
  printer()
  nombre = input('Ingrese el nombre del departamento: ')
  departamento = buscar_departamento(nombre)
  if departamento != None:
    #print('Menu editar departamento')
    #print('1.- Nombre') 
    #print('2.- Gerente')
    #print('0.- Salir')
    op = int(input('Seleccione una opción: '))
    if op == 1:
      #print(f'El nombre actual es: {departamento.getNombre()}')
      printer([
        ["El nombre actual es: " + departamento.getNombre(), None, None]
      ])
      nombre = input('Ingrese el nuevo nombre: ')
      departamento.setNombre(nombre)
    elif op == 2:
      #print(f'El gerente actual es: {departamento.getGerente()}')
      printer([
        ["El gerente actual es: " + departamento.getGerente(), None, None]
      ])
      gerente = input('Ingrese el nuevo gerente: ')
      departamento.setGerente(gerente)
    else:
      #print('No se realizaron cambios')
      printer(tipo=1,argumento="No se han realizado cambios.")
    actualizar_departamento(departamento)
  else:
    #print('Departamento no encontrado')
    printer(tipo=2,argumento="No se ha podido encontrar el departamento.")

def print_departamento():
  printer()
  nombre = input("Ingrese el nombre del departamento: ")
  departamento = buscar_departamento(nombre)
  if departamento != None:
    #print(departamento)
    printer([
      ["Departamento:\n",None,None],
      [departamento,None,None],
      ["Presiona ENTER para continuar...",None,None]
    ])
    input()
  else:
    #print('Departamento no encontrado')
    printer(tipo=2,argumento="Departamento no encontrado.")

def print_departamentos():
  departamentos = obtener_departamentos()
  if departamentos != None:
    if len(departamentos) > 0:
      printer()
      printer([
        ["Empleados:\n",None,None]
      ])
      for departamento in departamentos:
        #print(departamento)
        printer([
          [departamento,None,None]
        ])
      printer([
        ["Presiona ENTER para continuar...",None,None]
      ])
      input()
    else:
      #print('No hay departamentos ingresados')
      printer(tipo=1,argumento="No hay departamentos ingresados.")
  else:
    printer(tipo=2,argumento="Se ha producido un error a buscar los departamentos.")

def delete_departamento():
  printer()
  nombre = input("Ingrese el nombre del departamento: ")
  departamento = buscar_departamento(nombre)
  if departamento != None:
    #print(f'Eliminará  el departamento {departamento.getNombre()}')
    #print('¿Estás seguro?')
    #print('1.- Si')
    #print('2.- No')
    #print('0.- Salir')
    printer([
      ["Usted eliminará el departamento " + departamento.getNombre() + ".",None,None],
      ["Esta acción es irreversible. Está seguro?",None,None],
      ["1. Sí",None,None],
      ["2. No", None,None]
    ])
    resp = int(input('Seleccione una opción: '))
    if resp == 1:
      eliminar_departamento(departamento)
    else:
      #print('Departamento no eliminado')
      printer(tipo=1,argumento="El departamento no ha sido eliminado.")
  else:
    #print('Departamento no encontrado')
    printer(tipo=2,argumento="Departamento no encontrado.")  


def main_departamento():
  op = -1
  while op != 0:
    op = menu_departamento()
    if op == 1:
      add_departamento()
    elif op == 2:
      edit_departamento()
    elif op == 3:
      print_departamento()
    elif op == 4:
      print_departamentos()
    elif op == 5:
      delete_departamento()
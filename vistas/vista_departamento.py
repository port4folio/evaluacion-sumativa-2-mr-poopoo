from modelo.departamento import Departamento
from controlador.controlador_departamento import agregar_departamento, buscar_departamento, actualizar_departamento, obtener_departamentos, eliminar_departamento

def menu_departamento():
  print('-----------Menu Departamento-----------')
  print("1.- Agregar")
  print("2.- Editar")
  print("3.- Imprimir una")
  print("4.- Imprimir todas")
  print("5.- Eliminar")
  print("0.- Salir")
  op = int(input("Ingrese una opción: "))
  return op

def add_departamento():
  print('Ingrese los datos del departamento')
  nombre = input('Ingrese el nombre: ')
  descripcion= input('Ingrese descripcion: ')
  gerente = input('Ingrese el gerente: ')
  departamento = Departamento(nombre, descripcion, gerente)
  agregar_departamento(departamento)

def search_departamento():
  nombre = input('Ingrese el nombre del departamento: ')
  departamento = buscar_departamento(nombre)
  return departamento

def edit_departamento():
  departamento = buscar_departamento()
  if departamento is not None:
    print('Menu editar departamento')
    print('1.- Nombre') 
    print('2.- Gerente')
    print('0.- Salir')
    op = int(input('Seleccione una opción: '))
    if op == 1:
      print(f'El nombre actual es: {departamento.getNombre()}')
      nombre = input('Ingrese el nuevo nombre: ')
      departamento.setNombre(nombre)
    elif op == 2:
      print(f'El gerente actual es: {departamento.getGerente()}')
      gerente = input('Ingrese el nuevo gerente: ')
      departamento.setGerente(gerente)
    else:
      print('No se realizaron cambios')
    actualizar_departamento(departamento)
  else:
    print('Departamento no encontrado')

def print_departamento():
  departamento = buscar_departamento()
  if departamento is not None:
    print(departamento)
  else:
    print('Departamento no encontrado')

def print_departamentos():
  departamentos = obtener_departamentos()
  if len(departamentos) > 0:
    for departamento in departamentos:
      print(departamento)
  else:
    print('No hay departamentos ingresados')

def delete_departamento():
  departamento = buscar_departamento()
  if departamento is not None:
    print(f'Eliminará  el departamento {departamento.getNombre()}')
    print('¿Estás seguro?')
    print('1.- Si')
    print('2.- No')
    print('0.- Salir')
    resp = int(input('Seleccione una opción: '))
    if resp == 1:
      eliminar_departamento(departamento)
    else:
      print('Departamento no eliminado')
  else:
    print('Departamento no encontrado')  


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
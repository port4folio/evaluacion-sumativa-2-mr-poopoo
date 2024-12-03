from vistas.vista_empleado import main_empleado
#from vistas.vista_proyecto import main_pryecto
#from vistas.vista_departamento import main_departamento
#from vistas.vista_registro_tiempo import main_registro_tiempo

def informe():
    print("Informe principal")
    print("1.- Empleados")
    print("2.- Proyectos")
    print("3.- Departamentos")
    print("4.- Registro de tiempo")
    print("0.- Salir")
    print("Seleccione una opción: ")
    op=int(input("ingrese una opción: "))
    return op

while True:
    op=informe()
    if op==1:
        main_empleado()
    #elif op==2:
        #main_pryecto()
    #elif op==3:
       # main_departamento()
    #elif op==4:
       # main_registro_tiempo()
   # elif op==0:
        print("Gracias")
        break
    else:
        print("Debe seleccionar una opción válida")
        break
from blessed import Terminal

t = Terminal()

def printl(lista_texto):
    lista = list(lista_texto)
    for i in range(len(lista)):
        if lista[i][2] == None:
            lista[i][2] = ""
        if lista[i][1] == None:
            lista[i][2] = t.bright_white
        if lista[i][0] == None:
            lista[i][2] = "---"
        print(f"{lista[i][2]}{lista[i][1]}{lista[i][0]}{t.normal}")

def clean():
    return f"{t.home}{t.on_black}{t.clear}{t.home}"

def printw(texto):
    printl([
        ["AVISO",
         t.yellow,clean()],
        [str(texto),
         t.bright_yellow,None],
        ["Presione ENTER para continuar...",
         t.white,t.blink]
    ])
    input()

def printe(texto):
    printl([
        ["ALERTA",
         t.red,clean()],
        [str(texto),
         t.bright_red,None],
        ["Presione ENTER para continuar...",
         t.white,t.blink]
    ])
    input()

def prints(texto):
    printl([
        ["OPERACIÓN EXITOSA",
         t.green,clean()],
        [str(texto),
         t.bright_green,None],
        ["Presione ENTER para continuar...",
         t.white,t.blink]
    ])
    input()

def printer(argumento = None, tipo = None):
    match(tipo):
        case None:
            # Mostrar texto multilínea con formato
            if argumento != None:
                printl(argumento)
            else:
                # Limpiar pantalla
                printl([[clean(),None,None]])
        case 0:
            # Mostrar un éxito con una operación
            if argumento != None:
                prints(argumento)
            else:
                prints("La operación se ha realizado con éxito.")
        case 1:
            # Mostrar una alerta de un error leve
            if argumento != None:
                printw(argumento)
            else:
                printw("Ha habido un error leve en la aplicación.")
        case 2:
            # Mostrar una alerta de un error grave
            if argumento != None:
                printe(argumento)
            else:
                printe("Ha habido un error grave en la aplicación.")
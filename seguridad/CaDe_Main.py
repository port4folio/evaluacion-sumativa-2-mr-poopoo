#CaDe secure implementations
#made by camelydev

import seguridad.Calgorithm as Calgo      # Algoritmo custom que se basa en un número de movimientos para llegar al caracter en teclado qwerty
#import CaesarImp as Caesar     # Una simple implementación del cifrado Caesar. Aquí NO usaremos caesar, ya que reemplaza algunos caracteres como los números.
import seguridad.HashImp as Hash          # Una simple implementación del hash SHA256
import seguridad.MoliCipher as Moli       # Cifrado custom que se basa en reemplazar texto por números y puntos

def SecondChar(msg):
    #print(msg)
    ch = msg[3]
    #print(ch)
    return ord(ch)

def CaDeMain(entryMsg) -> str:
    calgoMsg = Calgo.CalgorithmEncode(entryMsg)
    moliMsg = Moli.MoliEncode(calgoMsg)
    hashMsg = Hash.HashEncode(moliMsg)
    finalMsg = str(hashMsg)
    return finalMsg
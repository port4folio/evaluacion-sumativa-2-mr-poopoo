# Molina's Cipher V0.2

import base64

def MoliEncode(msg):

    encText = ""

    str3 = msg.encode("ascii")
    prevText = base64.b64encode(str3).decode("ascii")

    i = 1
    for i in range(len(prevText)+1):
        match(prevText[i:i+1]):
            case "Q": encText = encText + "1."
            case "A": encText = encText + "11."
            case "Z": encText = encText + "111."
            case "W": encText = encText + "2."
            case "S": encText = encText + "22."
            case "X": encText = encText + "222."
            case "E": encText = encText + "3."
            case "D": encText = encText + "33."
            case "C": encText = encText + "333."
            case "R": encText = encText + "4."
            case "F": encText = encText + "44."
            case "V": encText = encText + "444."
            case "T": encText = encText + "5."
            case "G": encText = encText + "55."
            case "B": encText = encText + "555."
            case "Y": encText = encText + "6."
            case "H": encText = encText + "66."
            case "N": encText = encText + "666."
            case "U": encText = encText + "7."
            case "J": encText = encText + "77."
            case "M": encText = encText + "777."
            case "I": encText = encText + "8."
            case "K": encText = encText + "88."
            case "O": encText = encText + "9."
            case "L": encText = encText + "99."
            case "P": encText = encText + "0."
            case "Ñ": encText = encText + "00."
            case "=": encText = encText + "000."
            case "q": encText = encText + "1m."
            case "a": encText = encText + "11m."
            case "z": encText = encText + "111m."
            case "w": encText = encText + "2m."
            case "s": encText = encText + "22m."
            case "x": encText = encText + "222m."
            case "e": encText = encText + "3m."
            case "d": encText = encText + "33m."
            case "c": encText = encText + "333m."
            case "r": encText = encText + "4m."
            case "f": encText = encText + "44m."
            case "v": encText = encText + "444m."
            case "t": encText = encText + "5m."
            case "g": encText = encText + "55m."
            case "b": encText = encText + "555m."
            case "y": encText = encText + "6m."
            case "h": encText = encText + "66m."
            case "n": encText = encText + "666m."
            case "u": encText = encText + "7m."
            case "j": encText = encText + "77m."
            case "m": encText = encText + "777m."
            case "i": encText = encText + "8m."
            case "k": encText = encText + "88m."
            case "o": encText = encText + "9m."
            case "l": encText = encText + "99m."
            case "p": encText = encText + "0m."
            case "ñ": encText = encText + "00m."
            case "1": encText = encText + "1n."
            case "2": encText = encText + "2n."
            case "3": encText = encText + "3n."
            case "4": encText = encText + "4n."
            case "5": encText = encText + "5n."
            case "6": encText = encText + "6n."
            case "7": encText = encText + "7n."
            case "8": encText = encText + "8n."
            case "9": encText = encText + "9n."
            case "0": encText = encText + "0n."

    msg1 = encText.encode('ascii')
    finalText = base64.b64encode(msg1).decode("ascii")

    #print('MoliCipher:')
    #print(finalText)

    return finalText
# Camely's Algorithm V0.1

import base64 as bs

keyboardKeycells = [
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", "!"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "?"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
]

def CalgorithmEncode(msgToEncode):
    msgToEncode = str(msgToEncode)
    if (msgToEncode == ""):
        exit()
    modifiedMsg = msgToEncode.upper()
    moves = []
    asc = []
    finalText = ""
    for i in range(len(modifiedMsg)):
        movesDown = 0
        movesRight = 0
        for j in range(len(keyboardKeycells)):
            for k in range(len(keyboardKeycells[j])):
                gotError = False
                try:
                    keyCell = keyboardKeycells[j][k]
                except ValueError:
                    #print("no index found", j, k)
                    gotError = True
                if gotError == False:
                    if (keyCell == modifiedMsg[i]):
                        asc.append(ord(modifiedMsg[i]) + k)
                        movesDown = j
                        movesRight = k
                        #print(modifiedMsg[i])
        asc1 = asc[i]
        moves.append([movesDown,movesRight])
        #print(moves)
        v0Text = ""
        v1Text = ""
        for j in range(moves[i][0]):
            v0Text += "0"
        for k in range(moves[i][1]):
            v1Text += "1"
        t = v0Text + v1Text
        n = 4
        a = [t[i:i+n] for i in range(0, len(t), n)]
        #print(a)
        finalPos = ""
        fullText = ""
        for j in range(len(a)):
            if (len(a[j]) == 1):
                #1 Number
                finalPos += a[j]
            elif (len(a[j]) == 2):
                #2 Numbers
                pos0 = a[j][0:1]
                pos1 = a[j][1:2]
                #IF (POS 1 != POS 0) NEGATE ALL
                if (pos1 != pos0):
                    if (pos1 == "0"):
                        finalPos += "1"
                    else:
                        finalPos += "0"
                    
                    if (pos0 == "0"):
                        finalPos += "1"
                    else:
                        finalPos += "0"
                else:
                    finalPos += pos0 + pos1
            elif (len(a[j]) == 3):
                #3 Numbers
                pos0 = a[j][0:1]
                pos1 = a[j][1:2]
                pos2 = a[j][2:3]
                #Negate pos 1
                if pos1 == "0":
                    finalPos += "1"
                else:
                    finalPos += "0"
                if (pos0 == pos2):
                    finalPos += "1"
                else:
                    finalPos += "0"
                finalPos += pos2
            elif (len(a[j]) == 4):
                #4 Numbers
                pos0 = a[j][0:1]
                pos1 = a[j][1:2]
                pos2 = a[j][2:3]
                pos3 = a[j][3:4]
                if pos0 == "0":
                    finalPos += "1"
                else:
                    finalPos += "0"
                if (pos1 == "1" or pos2 == "1"):
                    finalPos += "1"
                else:
                    finalPos += "0"
                if (pos2 == pos3):
                    finalPos += "1"
                else:
                    finalPos += "0"
                finalPos += pos3
        finalPosBytes = finalPos.encode("ascii")
        finalB64Bytes = bs.b64encode(finalPosBytes)
        finalPos = finalB64Bytes.decode("ascii")
        fullText += finalPos
        asciiText = str(asc1)
        asciiBytes = asciiText.encode("ascii")
        b64Bytes = bs.b64encode(asciiBytes)
        b64Text = b64Bytes.decode("ascii")
        fullText += "-" + b64Text
        #print(fullText)
        finalText += fullText + ","
    #print('Calgorithm:')
    #print(finalText)

    return finalText
def Validar(s = str()):
    l, u, p, d = 0, 0, 0, 0
    if (len(s) >= 8):
        for i in s:

            # contar las letras lowercase
            if (i.islower()):
                l+=1

            # contar las letras uppercase
            if (i.isupper()):
                u+=1

            # contar digitos (numeros)
            if (i.isdigit()):
                d+=1

            # contar caracteres especiales
            if(i=='@' or i=='$' or i=='_' or i=='!' or i=='?' or i=='-' or i=='+'):
                p+=1
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)): #si la contraseña contiene todo lo mencionado, válida
        return True
    else: #y si no, inválida
        return False
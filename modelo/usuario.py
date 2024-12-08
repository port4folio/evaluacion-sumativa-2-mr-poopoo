
class Usuario:
    def __init__(self, id, correo, contraseña):
        self.__id= id
        self.__correo=correo
        self.__contraseña=contraseña
    
    def getId(self):
        return self.__id

    def getCorreo(self):
        return self.__correo    
    
    def getContraseña(self):
        return self.__contraseña
    
    def setId(self,id):
        self.__id= id
    
    def setCorreo(self,correo):
        self.__correo=correo
    
    def setContraseña(self,contraseña):
        self.__contraseña=contraseña


    def __str__(self):
        return f"Id: {self.__id}\nCorreo: {self.__correo}\n Contraseña: {self.__contraseña}"

class Usuario:
    def __init__(self, id, correo, contraseña):
        self.id= id
        self.correo=correo
        self.contraseña=contraseña
    
    def get_id(self):
        return self.__id

    def get_correo(self):
        return self.__correo    
    
    def get_contraseña(self):
        return self.__contraseña
    
    def set_id(self,id):
        self.__id= id
    
    def set_correo(self,correo):
        self.__correo=correo
    
    def set_contraseña(self,contraseña):
        self.__contraseña=contraseña


    def __str__(self):
        return f"Id: {self.__id}\nCorreo: {self.__correo}\n Contraseña: {self.__contraseña}"
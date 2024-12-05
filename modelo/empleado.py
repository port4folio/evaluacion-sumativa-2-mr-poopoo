from datetime import datetime

class Empleado:
    def __init__(self, nombres, paterno, materno, telefono, correo, direccion, comuna, fecha_inicio , sueldo):
        self.__id=0
        self.__nombres= nombres
        self.__paterno= paterno
        self.__materno= materno
        self.__telefono=telefono
        self.__correo=correo
        self.__direccion= direccion
        self.__comuna= comuna
        self.__id_departamento=0
        self.__fecha_inicio= fecha_inicio
        self.__sueldo=sueldo
        self.__proyecto=[]

    #getters
    def get_id(self):
        return self.__id
    
    def get_id_departamento(self):
        return self.__id_departamento

    def getNombres(self):
        return self.__nombres
    
    def getPaterno(self):
        return self.__paterno
    
    def getMaterno(self):
        return self.__materno
    
    def getTelefono(self):
        return self.__telefono
    
    def getCorreo(self):
        return self.__correo

    def getDireccion(self):
        return self.__direccion
    
    def get_comuna(self):
        return self.__comuna
       
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
    def get_sueldo(self):
        return self.__sueldo
    
    
    def get_proyecto(self):
        return self.__proyecto
    
    ##seters

    def set_id(self,id):
        self.__id=id
    
    def set_id_departamento(self,id_departamento):
        self.__id_departamento=id_departamento

    def set_nombres(self,nombres):
        self.__nombres=nombres
    
    def setDireccion(self,direccion):
        self.__direccion=direccion
    
    def setTelefono(self,telefono):
        self.__telefono=telefono

    def setCorreo(self,correo):
        self.__correo=correo
    
    def set_fecha_inicio(self,fecha_inicio):
        self.__fecha_inicio=fecha_inicio
    
    def set_sueldo(self,sueldo):
        self.__sueldo=sueldo

    def set_proyecto(self,proyecto):
        self.__proyecto=proyecto



    def __str__(self):
        return f"Nombre: {self.__nombres}\nDireccion: {self.__direccion}\nTelefono{self.__telefono}\nCorreo {self.__correo}\n {self.__fecha_inicio}\nSueldo {self.__sueldo}"
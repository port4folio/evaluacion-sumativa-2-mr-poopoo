from datetime import datetime

class Empleado:
    def __init__(self,nombre, direccion, telefono, correo, fecha_inicio , sueldo):
        self.__id= 0
        self.__nombre= nombre
        self.__direccion= direccion
        self.__telefono=telefono
        self.__correo=correo
        self.__fecha_inicio= fecha_inicio
        self.__sueldo=sueldo
        self.__departamento=None
        self.__proyecto=[]

    #getters
    def get_id(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def getCorreo(self):
        return self.__correo
    
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
    def get_sueldo(self):
        return self.__sueldo
    
    def get_departamento(self):
        return self.__departamento
    
    def get_proyecto(self):
        return self.__proyecto
    ##seters

    def set_id(self,id):
        self.__id=id

    def setNombre(self,nombre):
        self.__nombre=nombre
    
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
    
    def set_departamento(self,departamento):
        self.__departamento=departamento

    def set_proyecto(self,proyecto):
        self.__proyecto=proyecto



    def __str__(self):
        return f"Nombre: {self.__nombre}\nDireccion: {self.__direccion}\nTelefono{self.__telefono}\nCorreo {self.__correo}\n {self.__fecha_inicio}\nSueldo {self.__sueldo}"
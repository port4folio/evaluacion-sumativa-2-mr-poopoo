from datetime import datetime

class Empleado:
    def __init__(self, nombres, paterno, materno, telefono, correo, direccion, comuna, fecha_inicio, sueldo):
        self.__id=0
        self.__nombres= nombres
        self.__paterno= paterno
        self.__materno= materno
        self.__telefono=telefono
        self.__correo=correo
        self.__direccion=direccion
        self.__comuna=comuna
        self.__id_departamento=0
        self.__fecha_inicio=fecha_inicio
        self.__sueldo=sueldo
        self.__proyecto=[]

    #getters
    def getId(self):
        return self.__id
    
    def getId_departamento(self):
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
    
    def getComuna(self):
        return self.__comuna
       
    def getFecha_inicio(self):
        return self.__fecha_inicio
    
    def getSueldo(self):
        return self.__sueldo
    
    
    def getProyecto(self):
        return self.__proyecto
    
    ##seters

    def setId(self,id):
        self.__id=id
    
    def setId_departamento(self,id_departamento):
        self.__id_departamento=id_departamento

    def setNombres(self,nombres):
        self.__nombres=nombres
    
    def setPaterno(self,paterno):
        self.__paterno=paterno
    
    def setMaterno(self,materno):
        self.__materno=materno
    
    def setTelefono(self,telefono):
        self.__telefono=telefono

    def setCorreo(self,correo):
        self.__correo=correo

    def setDireccion(self,direccion):
        self.__direccion=direccion
    
    def setComuna(self,comuna):
        self.__comuna=comuna
    
    def setFecha_inicio(self,fecha_inicio):
        self.__fecha_inicio=fecha_inicio
    
    def setSueldo(self,sueldo):
        self.__sueldo=sueldo

    def setProyecto(self,proyecto):
        self.__proyecto=proyecto



    def __str__(self):
        return f"Nombres: {self.__nombres}\nPaterno: {self.__paterno}\nMaterno: {self.__materno}\nTelefono{self.__telefono}\nCorreo {self.__correo}\nDireccion: {self.__direccion}\nComuna: {self.__comuna}\nFecha de incio: {self.__fecha_inicio}\nSueldo {self.__sueldo}\n"
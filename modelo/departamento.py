class Departamento:
    def __init__(self,nombre,descripcion,gerente):
        self.__id_departamento= None
        self.__nombre = nombre
        self.__descripcion=descripcion
        self.__gerente = gerente
        self.__empleados = []

    def getId_departamento(self):
        return self.__id_departamento
    
    def getNombre(self):
        return self.__nombre
    
    def getDescripcion(self):
        return self.__descripcion

    def getGerente(self):
        return self.__gerente
    
    def getEmpleados(self):
        return self.__empleados


    def setId_departamento(self,id_departamento):
        self.__id_departamento=id_departamento

    def setNombre(self,nombre):
        self.__nombre=nombre 

    def setGerente(self,gerente):
        self.__gerente=gerente


    def __str__(self):
        return f"Nombre {self.__nombre}\nGerente {self.__gerente}"             
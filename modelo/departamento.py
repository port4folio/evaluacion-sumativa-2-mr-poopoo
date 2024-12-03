class Departamento:
    def __init__(self, id_departamento,nombre,descripcion,gerente):
        self.__id_departamento= id_departamento
        self.__nombre = nombre
        self.__descripcion=descripcion
        self.__gerente = gerente
        self.__empleados = []

    def get_id_departamento(self):
        return self.__id_departamento
    
    def get_nombre(self):
        return self.__nombre
    
    def get_descripcion(self):
        return self.__descripcion

    def get_gerente(self):
        return self.__gerente
    
    def get_empleados(self):
        return self.__empleados


    def set_id_departamento(self,id_departamento):
        self.__id_departamento=id_departamento

    def set_nombre(self,nombre):
        self.__nombre=nombre 

    def set_gerente(self,gerente):
        self.__gerente=gerente


    def __str__(self):
        return f"Nombre {self.__nombre}\nGerente {self.__gerente}"             
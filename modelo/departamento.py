class Departamento:
    def __init__(self,nombre,descripcion,gerente):
        self.__id=0
        self.__nombre = nombre
        self.__descripcion=descripcion
        self.__gerente = gerente
        self.__empleados = []

    def get_id(self):
        return self.__id
    

    def get_nombre(self):
        return self.__nombre
    
    def get_descripcion(self):
        return self.__descripcion

    def get_gerente(self):
        return self.__gerente
    

    def get_empleados(self):
        return self.__empleados


    def set_id(self,id):
        self.__id=id

    def set_nombre(self,nombre):
        self.__nombre=nombre 

    def set_gerente(self,gerente):
        self.__gerente=gerente


    def agregar_empleado(self,empleado):
        if empleado.departamento != self:
            empleado.asignar_departamento(self)
            self.empleados.append(empleado)

    def eliminar_empleado(self, empleado):
        if empleado in self.empleados:
            self.empleados.remove(empleado)
            empleado.asiganr_departamento(None)

    def __str__(self):
        return f"Nombre {self.__nombre}\nGerente {self.__gerente}"             
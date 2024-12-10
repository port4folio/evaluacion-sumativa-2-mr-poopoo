class Proyecto:
    def __init__(self, nombre_proyecto,descripcion_proyecto,fecha_inicio):
        self.__id=0
        self.__nombre_proyecto=nombre_proyecto
        self.__descripcion_proyecto=descripcion_proyecto
        self.__fecha_inicio=fecha_inicio
        self.__empleado=[]

    def get_id(self):
        return self.__id

    def get_nombre_proyecto(self):
        return self.__nombre_proyecto
    
    def get_descripcion_proyecto(self):
        return self.__descripcion_proyecto
    
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
    def get_empleado(self):
        return self.__empleado
    
    def set_id(self,id):
        self.__id=id
    
    def set_nombre_proyecto(self,nombre_proyecto):
        self.__nombre_proyecto=nombre_proyecto

    def set_descripcion_proyecto(self,descripcion_proyecto):
        self.__descripcion_proyecto=descripcion_proyecto
    
    def set_fecha_inicio(self,fecha_inicio):
        self.__fecha_inicio=fecha_inicio

    def set_empleado(self,empleado):
        self.__empleado=empleado
    

    def __str__(self):
        return f"Nombre: {self.__nombre}\nDescripcion del proyecto {self.__descripcion_proyecto}\nFecha de inicio {self.__fecha_inicio}\n"
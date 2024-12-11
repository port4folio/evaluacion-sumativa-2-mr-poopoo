class Proyecto:
    def __init__(self, nombre_proyecto,descripcion_proyecto,fecha_inicio):
        self.__id=0
        self.__nombre_proyecto=nombre_proyecto
        self.__descripcion_proyecto=descripcion_proyecto
        self.__fecha_inicio=fecha_inicio
        self.__empleado=[]

    def getId(self):
        return self.__id

    def getNombre_proyecto(self):
        return self.__nombre_proyecto
    
    def getDescripcion_proyecto(self):
        return self.__descripcion_proyecto
    
    def getFecha_inicio(self):
        return self.__fecha_inicio
    
    def getEmpleado(self):
        return self.__empleado
    
    def setId(self,id):
        self.__id=id
    
    def setNombre_proyecto(self,nombre_proyecto):
        self.__nombre_proyecto=nombre_proyecto

    def setDescripcion_proyecto(self,descripcion_proyecto):
        self.__descripcion_proyecto=descripcion_proyecto
    
    def setFecha_inicio(self,fecha_inicio):
        self.__fecha_inicio=fecha_inicio

    def setEmpleado(self,empleado):
        self.__empleado=empleado
    

    def __str__(self):
        return f"Nombre: {self.__nombre}\nDescripcion del proyecto {self.__descripcion_proyecto}\nFecha de inicio {self.__fecha_inicio}"
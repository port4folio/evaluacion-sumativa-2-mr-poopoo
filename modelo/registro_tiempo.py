class Registro_tiempo:
    def __init__(self, id_empleado, id_proyecto, fecha, hra_entrada, hra_salida, hrs_trabajadas, descripcion_tareas):
        self.__fecha=fecha
        self.__id_empleado=id_empleado
        self.__id_proyecto=id_proyecto
        self.__hra_entrada=hra_entrada
        self.__hra_salida=hra_salida
        self.__hrs_trabajadas=hrs_trabajadas
        self.__descripcion_tareas=descripcion_tareas
        self.__id_registro = 0

    #def get_empleado(self):
    #return self.__empleado ???
    
    def getFecha(self):
        return self.__fecha
    
    def getId(self):
        return self.__id_registro
    
    def getId_empleado(self):
        return self.__id_empleado
    
    def getId_proyecto(self):
        return self.__id_proyecto
    
    def get_hra_entrada(self):
        return self.__hra_entrada
    
    def get_hra_salida(self):
        return self.__hra_salida
    
    def get_hrs_trabajadas(self):
        return self.__hrs_trabajadas
    
    def getDescripcion_tareas(self):
        return self.__descripcion_tareas
    
    def setId(self, id_registro):
        self.__id_registro = id_registro

    def setFecha(self,fecha):
        self.__fecha=fecha
    
    def setId_empleado(self,id_empleado):
        self.__id_empleado=id_empleado
    
    def setId_proyecto(self,id_proyecto):
        self.__id_proyecto=id_proyecto
    
    def set_hra_entrada(self,hra_entrada):
        self.__hra_entrada=hra_entrada
    
    def set_hra_salida(self,hra_salida):
        self.__hra_salida=hra_salida
        
    def setHrs_trabajadas(self,hrs_trabajadas):
        self.__hrs_trabajadas=hrs_trabajadas
    
    def setDescripcion_tareas(self,descripcion_tareas):
        self.__descripcion_tareas=descripcion_tareas

    def __str__(self):
        return f"Trabajo desde las {self.__hra_entrada} con un total de {self.__hrs_trabajadas}horas terminando a las {self.__hra_salida}, el dia {self.__fecha}en el proyecto N°{self.__id_proyecto}"


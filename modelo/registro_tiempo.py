class registro_tiempo:
    def __init__(self,empleado, fecha, horas_trabajadas, descripcion, proyecto):
        self.__empleado=empleado
        self.__fecha=fecha
        self.__horas_trabajadas=horas_trabajadas
        self.__descripcion=descripcion
        self.__proyecto=proyecto

    def get_empleado(self):
        return self.__empleado
    
    def get_fecha(self):
        return self.__fecha
    
    def get_horas_trabajadas(self):
        return self.__horas_trabajadas
    
    def get_descripcion(self):
        return self.__descripcion
    
    def get_proyecto(self):
        return self.__proyecto
    

    def set_empleado(self,empleado):
        self.__empleado=empleado
    
    def set_fecha(self,fecha):
        self.__fecha=fecha
    
    def set_horas_trabajadas(self,horas_trabajadas):
        self.__horas_trabajadas=horas_trabajadas
    
    def set_descripcion(self,descripcion):
        self.__descripcion=descripcion
    
    def set_proyecto(self,proyecto):
        self.__proyecto=proyecto


    def __str__(self):
        return f"{self.__empleado}trabajo {self.__horas_trabajadas}horas,   el dia {self.__fecha}en el proyecto {self.__proyecto}"


class registro_tiempo:
    def __init__(self,id_empleado, fecha, hrs_trabajadas, descripcion_tareas, id_proyecto):
        self.__fecha=fecha
        self.__id_empleado=id_empleado
        self.__id_proyecto=id_proyecto
        self.__hrs_trabajadas=hrs_trabajadas
        self.__descripcion_tareas=descripcion_tareas
        #asdasdasdasd
        # dfsksdhfhdf

        self.__hrs_trabajadas=hrs_trabajadas
        self.__descripcion_tareas=descripcion_tareas
        self.__id_proyecto=id_proyecto

    def get_empleado(self):
        return self.__empleado
    
    def get_fecha(self):
        return self.__fecha
    
    def get_id_empleado(self):
        return self.__id_empleado
    
    def get_id_proyecto(self):
        return self.__id_proyecto
    
    def get_hrs_trabajadas(self):
        return self.__hrs_trabajadas
    
    def get_descripcion_tareas(self):
        return self.__descripcion_tareas
    

    def set_fecha(self,fecha):
        self.__fecha=fecha
    
    def set_id_empleado(self,id_empleado):
        self.__id_empleado=id_empleado
    
    def set_id_proyecto(self,id_proyecto):
        self.__id_proyecto=id_proyecto
        
    def set_hrs_trabajadas(self,hrs_trabajadas):
        self.__hrs_trabajadas=hrs_trabajadas
    
    def set_descripcion_tareas(self,descripcion_tareas):
        self.__descripcion_tareas=descripcion_tareas
    


    def __str__(self):
        return f"{self.__empleado}trabajo {self.__horas_trabajadas}horas,   el dia {self.__fecha}en el proyecto {self.__id_proyecto}"


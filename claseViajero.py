class ViajeroFrecuente:
    def __init__(self, num, dni, nombre, apellido, millas):
        self.__num_viajero=num
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas

    def cantidadTotalMillas(self):
        return self.__millas_acum

    def acumularMillas(self, millas):
        self.__millas_acum+=millas
        return self.__millas_acum

    def canjearMillas(self, millascanj):
        if millascanj<=self.__millas_acum:
            self.__millas_acum-=millascanj
            return self.__millas_acum
        else: print ("Error")
        
    def getNumViajero(self):
        return self.__num_viajero
            






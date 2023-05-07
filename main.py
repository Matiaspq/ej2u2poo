from claseManejadorViajero import ManejadorClaseViajero
if __name__== '__main__':
    v=ManejadorClaseViajero()
    v.cargaViajero()
    num=int(input("Ingresa numero de viajero: "))
    v.buscaViajero(num)
    

import csv
from claseViajero import ViajeroFrecuente
from menu import menu
class ManejadorClaseViajero:
    def __init__(self):
        self.__viajeros=[]

    def cargaViajero(self):
        archivo = open('viajerofrecuente.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            viajero=ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
            self.__viajeros.append(viajero)

    def buscaViajero(self,num):
        i = 0
        while i < len(self.__viajeros) and self.__viajeros[i].getNumViajero() != num:
            i+=1
        menu(self.__viajeros[i],num)
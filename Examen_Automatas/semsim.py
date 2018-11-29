#Programador: Jefferson Alvarez Lopez
#Como solo se va a hacer AVERAGE o Var entonces solo verfico que en recorrido no hayan letras

#MODULOS
from semantic import *
import sys


class semsim:

    def __init__(self, estructura):
        self.estructura = estructura
        self.matriz = []
        self.valoresFinales = []

    def run(self):
        print('Semsim : RUN')
        self.analizarTabla(self.estructura.tabla)
        self.analizarFuncion(self.estructura.funcion)
        print('VALORES FINALES', self.valoresFinales)

    def analizarTabla(self, tabla):
        for fila in tabla.filas:
            self.matriz.append(fila.valores)
            print(fila.valores)

    def analizarFuncion(self, funcion):
        for argumento in funcion.argumentos.listaArgumentos:
            if(isinstance(argumento, semantic.p_rango)):
                self.analizarRango(argumento)
            elif (isinstance(argumento, semantic.p_celda)):
                self.analizarCelda(argumento)      
            else:
                self.valoresFinales.append(argumento)

    def analizarRango(self, rango):
        celda1 = rango.celda1
        celda2 = rango.celda2
        if(celda1[0] > celda2[0]):
            filaMenor = celda2[0]
            filaMayor = celda1[0]
        else:
            filaMenor = celda1[0]
            filaMayor = celda2[0]

        if(celda1[1] > celda2[1]):
            columnaMenor = celda2[1]
            columnaMayor = celda1[1]
        else:
            columnaMenor = celda1[1]
            columnaMayor = celda2[1]

        #METODO DE LOS FINOS
        for itr in range (filaMenor, filaMayor+1):
            for itr2 in range (columnaMenor, columnaMayor+1):
                if(str(self.matriz[itr][itr2]).isalpha()):
                    print('ERROR:','LA FUNCION NO PUEDE MANEJAR CARACTERES ALFABETICOS')
                    sys.exit(-1)
                else:
                    valor = self.matriz[itr][itr2]
                    self.valoresFinales.append(valor)
    
    def analizarCelda(self, celdaEntrada):
        celda = celdaEntrada.celda
        if(str(self.matriz[celda[0]][celda[1]]).isalpha()):
            print('ERROR:','LA FUNCION NO PUEDE MANEJAR CARACTERES ALFABETICOS')
            sys.exit(-1)
        else:
            valor = self.matriz[celda[0]][celda[1]]
            self.valoresFinales.append(valor)
#Programador: Jefferson Alvarez Lopez
import semantic
import sys


#CONSTANTES
A = 0
B = 1
C = 2
D = 3
E = 4

#CLASE

class p_excel_ejecutor():
    def __init__(self, tabla, funcion):
        self.tabla = tabla
        self.funcion = funcion

class p_tabla():
    def __init__(self, fila1, fila2, fila3, fila4, fila5):
        self.filas = [fila1, fila2, fila3, fila4, fila5]
    
    def printSelf(self):
        for fila in self.filas:
            fila.printSelf()

class p_fila():
    def __init__(self, valor1, valor2, valor3, valor4, valor5):
        self.valores = [valor1, valor2, valor3, valor4, valor5]
    
    def printSelf(self):
        for val in self.valores:
            print('Valor:', val, type(val))

class p_funcion():
    def __init__(self, tipo, argumentos):
        self.tipo = tipo
        self.argumentos = argumentos

    def printSelf(self):
        print('Tipo_Funcion:', tipo)

class p_argumentos():
    def __init__(self):
        self.listaArgumentos = list()

    def printSelf():
        for argumentos in self.listaArgumentos:
            print(argumentos)

class p_rango():
    def __init__(self, celda1, celda2):
        self.celda1 = self.determinarIndice(celda1)
        self.celda2 = self.determinarIndice(celda2)

    def determinarIndice(self, celda):
        letra = 4
        if(celda[0] == 'A'):
            letra = A
        elif(celda[0] == 'B'):
            letra = B
        elif(celda[0] == 'C'):
            letra = C
        elif(celda[0] == 'D'):
            letra = D
        real = [int(celda[1]), letra]
        return real

    def printSelf():
        pass

class p_celda():
    def __init__(self, celda):
        self.celda = self.determinarIndice(celda)

    def determinarIndice(self, celda):
        letra = 4
        if(celda[0] == 'A'):
            letra = A
        elif(celda[0] == 'B'):
            letra = B
        elif(celda[0] == 'C'):
            letra = C
        elif(celda[0] == 'D'):
            letra = D
        real = [int(celda[1]), letra]
        return real
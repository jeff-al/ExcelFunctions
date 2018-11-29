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
        self.tipo = ''

    def run(self):
        print('Semsim : RUN')
        self.analizarTabla(self.estructura.tabla)
        self.analizarFuncion(self.estructura.funcion)
        if(self.tipo.upper() == 'AVERAGE'):
            self.crearAverage()
        else:
            self.crearVar()
        print('VALORES FINALES', self.valoresFinales)

    def analizarTabla(self, tabla):
        for fila in tabla.filas:
            self.matriz.append(fila.valores)
            print(fila.valores)

    def analizarFuncion(self, funcion):
        self.tipo = funcion.tipo
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

    def crearAverage(self):
        print('Es average')
        salida = open('output.s', 'w+')
        salida.write('.data\n')              #DATOS A PARTIR DE AQUI
        salida.write('\tarray:\t.word ')
        
        for item in range(len(self.valoresFinales)-1):
            salida.write(str(self.valoresFinales[item]) + ', ')
        salida.write(str(self.valoresFinales[-1])+'\n')
        salida.write('\tlength:\t.word ' + str(len(self.valoresFinales)) + '\n')
        salida.write('\tsum:\t.word 0\n')
        salida.write('\taverage:\t.word 0\n')
        
        
        
        salida.write('.text\n')                 #TEXT A PARTIR DE AQUI
        salida.write('\tmain:\n')
        salida.write('\tla $t0, array\n\tli $t1, 0\n\tlw $t2, length\n\tli $t3, 0\n') #VARIABLES NECESARIAS
       
        salida.write('\tsumLoop:\n')            #CICLO PARA HACER EL CALCULO
        salida.write('\t\tlw $t4, ($t0)\n')
        salida.write('\t\tadd $t3, $t3, $t4\n')
        salida.write('\t\tadd $t1, $t1, 1\n')
        salida.write('\t\tadd $t0, $t0, 4\n')
        salida.write('\t\tblt $t1, $t2, sumLoop\n')
        salida.write('\tsw $t3, sum\n\n')

        salida.write('\tli $v0, 1\n')  #DESPLEGAR LA SUMA
        salida.write('\tmove $a0, $t3\n')
        salida.write('\tsyscall\n\n')  

        salida.write('\tdiv $t5, $t3, $t2\n')   #CALCULAR PROMEDIO
        salida.write('\tsw $t5, average\n\n')
        
        salida.write('\tli $v0, 1\n')  #DESPLEGAR El PROMEDIO
        salida.write('\tmove $a0, $t5\n')
        salida.write('\tsyscall\n\n')  

        salida.write('\tli $v0, 10\n\tsyscall')
        salida.close() 

    def crearVar(self):
        print('Es var')
        pass
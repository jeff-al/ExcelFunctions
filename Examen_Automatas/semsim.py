#Programador: Jefferson Alvarez Lopez
#Como solo se va a hacer AVERAGE o Var entonces solo verfico que en recorrido no hayan letras
#

#MODULOS
import syntacticStructure
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
            if(isinstance(argumento, syntacticStructure.p_rango)):
                self.analizarRango(argumento)
            elif (isinstance(argumento, syntacticStructure.p_celda)):
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
        salida.write('.data\n'+         #DATOS
        '\tarray:\t.double ')
        
        for item in range(len(self.valoresFinales)-1):
            salida.write(str(self.valoresFinales[item]) + ', ')
        salida.write(str(self.valoresFinales[-1])+'\n'+
        '\tlength:\t.double ' + str(len(self.valoresFinales)) + '\n'+
        '\tlength1:\t.word ' + str(len(self.valoresFinales)) + '\n'+
        '\tsum:\t.double 0\n'+
        '\taverage:\t.double 0\n')
        
        
        
        salida.write('.text\n'+      #VARIABLES NECESARIAS
        '\tmain:\n'+
        '\tla $t0, array\n'+
        '\tli $t1, 0\n'+
        '\tldc1 $f2, length\n'+
        '\tlw $t2, length1\n'+
        '\tldc1 $f4, sum\n')
       
        salida.write('\tsumLoop:\n'+            #CICLO PARA HACER EL CALCULO
        '\t\tldc1 $f6, ($t0)\n'+
        '\t\tadd.d $f4, $f4, $f6\n'+
        '\t\tadd $t1, $t1, 1\n'+
        '\t\tadd $t0, $t0, 8\n'+
        '\t\tblt $t1, $t2, sumLoop\n'+
        '\tswc1 $f4, sum\n\n'+
        '\t#li $v0, 3\n'+
        '\t#mov.d $f12, $f4\n'+
        '\t#syscall\n\n'+
        '\tdiv.d $f6, $f4, $f2\n'+
	    '\tswc1 $f6, average\n'+
        '\tli $v0, 3\n'+
        '\tmov.d $f12, $f6\n'+
        '\tsyscall\n\n')   

        salida.close() 

    def crearVar(self):
        salida = open('output.s', 'w+')
        salida.write('.data\n'+         #DATOS
        '\tarray:\t.double ')
        
        for item in range(len(self.valoresFinales)-1):
            salida.write(str(self.valoresFinales[item]) + ', ')
        salida.write(str(self.valoresFinales[-1])+'\n'+
        '\tlength:\t.double ' + str(len(self.valoresFinales)) + '\n'+
        '\tlength1:\t.word ' + str(len(self.valoresFinales)) + '\n'+
        '\tsum:\t.double 0\n'+
        '\taverage:\t.double 0\n'+
        '\tvar:\t.double 0\n')
        
        
        
        salida.write('.text\n'+      #VARIABLES NECESARIAS
        '\tmain:\n'+
        '\tla $t0, array\n'+
        '\tli $t1, 0\n'+
        '\tldc1 $f2, length\n'+
        '\tlw $t2, length1\n'+
        '\tldc1 $f4, sum\n')
       
        salida.write('\tsumLoop:\n'+            #CICLO PARA HACER EL CALCULO
        '\t\tldc1 $f6, ($t0)\n'+
        '\t\tadd.d $f4, $f4, $f6\n'+
        '\t\tadd $t1, $t1, 1\n'+
        '\t\tadd $t0, $t0, 8\n'+
        '\t\tblt $t1, $t2, sumLoop\n'+
        '\tswc1 $f4, sum\n\n'+
        '\t#li $v0, 3\n'+
        '\t#mov.d $f12, $f4\n'+
        '\t#syscall\n\n'+
        '\tdiv.d $f6, $f4, $f2\n'+
	    '\tswc1 $f6, average\n'+
        '\tmov.d $f8, $f6\n\n'+
        '\t#li $v0, 3\n'+
        '\t#mov.d $f12, $f8\n'+
        '\t#syscall\n\n')  

        salida.write('\tla $t0, array\n'+ #VARIABLES NECESARIAS
        '\tli $t1, 0\n'+
        '\tldc1 $f2, length\n'+
        '\tlw $t2, length1\n'+
        '\tldc1 $f10, var\n') 

        salida.write('	devLoop:\n'+ #LOOP
		'\t\tldc1 $f6, ($t0)\n'+
		'\t\tsub.d $f4, $f6, $f8\n' +
		'\t\tmul.d $f4, $f4, $f4\n' +
		'\t\tadd.d $f10, $f10, $f4\n' +
		'\t\tadd $t1, $t1, 1\n' +
        '\t\tadd $t0, $t0, 8\n' +
		'\t\tblt $t1, $t2, devLoop\n')

        salida.write('\tswc1 $f10, sum\n\n'+ #FIN
	    '\tdiv.d $f10, $f10, $f2\n'+
    	'\tswc1 $f10, average\n\n'+
	    '\tli $v0, 3\n'+
	    '\tmov.d $f12, $f10\n'+
	    '\tsyscall\n\n'+
	    '\tli $v0, 10\n'+
	    '\tsyscall')

        salida.close() 

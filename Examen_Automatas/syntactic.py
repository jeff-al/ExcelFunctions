#Programador: Jefferson Alvarez
#Suposiciones: Matrices de tamano fijo 5x5
# - Vienen Saltos de linea despues de cada fila.

#MODULOS

import ply.yacc as yacc
import argparse
import sys
import syntacticStructure
import semsim


#TOKENS DEL ANALIZADOR LEXICO

from lexical import tokens

#VARIABLES GLOBALES (TALVEZ SE OCUPEN)
estructuraPrincipal = None
errorSintactico = False

#PRODUCCION PRINCIPAL

def p_excel_ejecutor(p):
    '''excel_ejecutor : tabla funcion'''
    global errorSintactico
    if(not errorSintactico):
        estructuraPrincipal = syntacticStructure.p_excel_ejecutor(p[1],p[2])
        semsimP = semsim.semsim(estructuraPrincipal)
        semsimP.run()
        #print('Sigue asi CRACK')

def p_tipo_entrada(p):
    '''tipo_entrada : CARACTER
    | NUMERO_ENTERO
    | NUMERO_REAL 
    '''
    if(str(p[1]).isalpha()):
        p[0] = str(p[1])
    elif (str(p[1]).__contains__(".")):
        p[0] = float(p[1])
    else:
        p[0] = int(p[1]) 
    #print('tipo_entrada')

def p_rango(p):
    ''' rango : CELDA DOS_PUNTOS CELDA'''
    estructuraPrincipal = syntacticStructure.p_rango(p[1], p[3])
    p[0] = estructuraPrincipal
    #print('rango')

def p_tipo_argumento(p):
    '''tipo_argumento : NUMERO_ENTERO
    | NUMERO_REAL
    | rango
    | CELDA
     '''
    
    if (isinstance(p[1], syntacticStructure.p_rango)):
        p[0] = p[1]
    elif (str(p[1]).__contains__(".")):
        p[0] = float(p[1])
    elif(str(p[1]).isnumeric() or str(p[1]).__contains__("-")):
        p[0] = int(p[1])
    else:
        estructuraPrincipal = syntacticStructure.p_celda(p[1])
        p[0] = estructuraPrincipal
    #print('tipo_argumento')

def p_tabla(p):
    '''tabla : PAL_ITABLE fila fila fila fila fila PAL_ETABLE '''
    estructuraPrincipal = syntacticStructure.p_tabla(p[2], p[3], p[4], p[5], p[6])
    p[0] = estructuraPrincipal
    #print('tabla')

def p_fila(p):
    '''fila : tipo_entrada COMA tipo_entrada COMA tipo_entrada COMA tipo_entrada COMA tipo_entrada'''
    estructuraPrincipal = syntacticStructure.p_fila(p[1], p[3], p[5], p[7], p[9])
    p[0] = estructuraPrincipal
    #print('fila')

def p_funcion(p):
    '''funcion : PAL_IFUNCTION IGUAL tipo_func PARENTESIS_ABIERTO argumentos PARENTESIS_CERRADO PAL_EFUNCTION'''
    estructuraPrincipal = syntacticStructure.p_funcion(p[3], p[5])
    p[0] = estructuraPrincipal
    #print('funcion')

def p_tipo_func(p):
    '''tipo_func : AVERAGE
    | VAR '''
    p[0] = p[1]
    #print('tipo_func')

def p_argumentos(p):
    '''argumentos : tipo_argumento extension_arg'''
    p[2].listaArgumentos.insert(0, p[1])
    p[0] = p[2]
    #print('argumentos')

def p_extension_arg(p):
    ''' extension_arg : COMA argumentos
    | vacio
    '''
    if(p[1] == None):
        p[0] = syntacticStructure.p_argumentos()
    else:
        p[0] = p[2]
    #print('extension_arg')

def p_vacio(p):
    '''vacio : '''
    p[0] = None
    #print('VACIO')


###########################################REUTILIZO######################################


# Regla para el error (Reutilizado del proyecto)
def p_error(p):
    global errorSintactico
    errorSintactico = True
    try:
        print("\nSe detectó un error en la sintaxis cerca de: \nTipo del token : "+ str(p.type) + "\nValor del token : " + str(p.value) + "\nLínea en el código : " + str(p.lineno) + "\nColumna en el código : "+ str(find_column(data,p)) + "\n")
    except Exception as e:
        print("\nSe detectó un error en la sintaxis")

def printError():
    print("Could not open the inputfile")

# Determinar el número de columna de un token
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Argument parser
argparser = argparse.ArgumentParser(description='choose the type of node you want to use')
argparser.add_argument("inputfile", help="recive a path to the input file")
args = argparser.parse_args()
#print ("inputfile: " + args.inputfile)

iF = open(args.inputfile, 'r')
if(iF.mode != 'r'):
    printError()
    sys.exit(-1)

data = iF.read()

# Construyo el parser
yaccer = yacc.yacc()
yaccer.parse(data)

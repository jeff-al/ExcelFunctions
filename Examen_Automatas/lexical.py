#Programador: Jefferson Alvarez Lopez
#Suposiciones: Las funciones vienen o solo mayusculas o solo minusculas
#
#

#MODULOS

import sys, getopt
import ply.lex as lex

#NOMBRE DE LOS TOKENS

tokens = [
    'PARENTESIS_ABIERTO',
    'PARENTESIS_CERRADO',
    'COMA',
    'DOS_PUNTOS',
    'IGUAL',
    'AVERAGE',
    'VAR',
    'CARACTER',
    'NUMERO_ENTERO',
    'NUMERO_REAL',
    'CELDA',
    'PAL_ITABLE',      #ETIQUETA PARA EL INICIO DE TABLA
    'PAL_ETABLE',      #ETIQUETA PARA EL FIN DE TABLA
    'PAL_IFUNCTION',#ETIQUETA PARA EL INICIO DE FUNCION
    'PAL_EFUNCTION', #ETIQUETA PARA EL FIN DE FUNCION
]

# EXPRESIONES REGULARES

#TOKENS SIMPLES
t_PAL_ITABLE            = r'ITABLE\:'
t_PAL_ETABLE            = r'ETABLE\:'
t_PAL_IFUNCTION         = r'IFUNCTION\:'
t_PAL_EFUNCTION         = r'EFUNCTION\:'
t_CELDA                 = r'[A-E][0-4]'
t_PARENTESIS_ABIERTO    = r'\('
t_PARENTESIS_CERRADO    = r'\)'
t_COMA                  = r'\,'
t_DOS_PUNTOS            = r'\:'
t_IGUAL                 = r'\='
t_CARACTER              = r'[a-zA-Z]'
t_AVERAGE               = r'(AVERAGE)|(average)'
t_VAR                   = r'(VAR)|(var)'

#CON ACCIONES (REUTILIZADAS DEL PROYECTO)

def t_NUMERO_REAL(t):
    r'-?[\d]+\.[\d][\d]?'
    t.value = float(t.value)
    return t

def t_NUMERO_ENTERO(t):
    r'-?[\d]+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("¡Illegal character: '%s'!" % t.value[0])
    sys.exit(-1)
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'
    




#############################PRUEBAS#####################################################

'''def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        printHelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help':
            printHelp()
            sys.exit()
        elif opt == "-i":
            inputfile = arg
    #print 'Input file is "%s"' %inputfile

    # Se debe abrir el archivo pasado por consola
    
    # Primero se verifica que el ususario haya pasado un archivo de entrada.
    # Si no es el caso se imprime un mensaje de error en consola.
    if not inputfile:
        print('ERROR')
        return
    
    # Si el usuario paso un archivo de entrada
    # Se intenta habrir el archivo
    # Si el archivo no se pudo habrir se imprime un mensaje de error en consola.
    iF = open(inputfile, 'r')
    if(iF.mode != 'r'):
        print('ERROR')
        return

    # Si el archivo es valido
    # Uso de lex
    lexer = lex.lex()

    data = iF.read()
    #print(data)

    lexer.input(data)
    for tok in lexer:
        print('Token: ' + str(tok.value) + '\n' + 'Tipo: ' + str(tok.type) + '\n')    

if __name__ == "__main__":
   main(sys.argv[1:])
'''
lexer = lex.lex()
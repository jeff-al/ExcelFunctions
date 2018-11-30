#Programador: Jefferson Alvarez Lopez
#Suposiciones: 
# - Las funciones vienen solo mayusculas o solo minusculas
# - Las filas empiezan en 0 y no en 1. 
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
    
lexer = lex.lex()
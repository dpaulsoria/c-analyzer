from lexical import tokens
import ply.yacc as yacc


def p_EXPRESSION(p):
    """
    EXPRESSION : COMENTARIOLEX
                | VARIABLELEX 
                | OPERATION
                | DECLARATION
                | SENTENCIAS
                | INCLUDE


    """
    p[0] = ('EXPRESSION', p[1])


# START GABRIELA RAMOS
def p_INCLUDE(p):
  """
    INCLUDE : PP_INCLUDE LESS_THAN HEADER_LIB GREATER_THAN 
              | PP_INCLUDE DOUBLE_APOS HEADER_LIB DOUBLE_APOS
  """


def p_VALUE(p):
    """
    VALUE : INTEGER
            | DECIMAL
    """ 
    p[0] = ('VALUE', p[1])


def p_SENTENCIAS(p):
    """
    SENTENCIAS : IF
                | ELSEIF
                | ELSE
                | FOR
                | WHILE
                | SWITCH
    """
    p[0] = ('SENTENCIAS',p[1])


def p_DATA_TYPE(p):
    """
    DATA_TYPE : INT 
                | FLOAT
                | LONG 
                | DOUBLE
                | CHAR
                | SHORT           
    """
    p[0] = ('DATA_TYPE',p[1])

def p_DECLARATION(p):
    """
    DECLARATION : DATA_TYPE VARNAME EQUAL INTEGER
    """
    p[0] = ('DECLARATION',p[1])

# END GABRIELA RAMOS


def p_COMENTARIOLEX(p):
    """
    COMENTARIOLEX : COMMENT
    """
    p[0] = ('COMMENT', p[1])


def p_VARIABLELEX(p):
    """
    VARIABLELEX : VARNAME
    """
    p[0] = ('VARNAME', p[1])


def p_OPERADOR(p):
    """
    OPERADOR : PLUS
              | MINUS
              | TIMES
              | MODULUS
              | DIVIDE
    """
    p[0] = ('OPERADOR', p[1])


def p_OPERATION(p):
    """
    OPERATION : VALUE OPERADOR VALUE
    """
    p[0] = ('OPERATION', p[1])


def p_error(p):
    print("Syntax error in input", p)


# Build the parser
parser = yacc.yacc()


def syntax():
    while True:
        try:
            s = input('parser > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result)


def syntactic_analyzer(data):
    return parser.parse(data)


syntax()

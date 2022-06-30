from lexicon import tokens
import ply.yacc as yacc


def p_EXPRESSION(p):
    """
    EXPRESSION : COMENTARIOLEX
                | VARIABLELEX 
                | OPERATION
                | DECLARATION
                | SENTENCIAS
                | INCLUDE
                | PREPROCCESOR_DIRECTIVE

    """
    p[0] = ('EXPRESSION', p[1])


# START GABRIELA RAMOS
def p_PREPROCCESOR_DIRECTIVE(p):
    """
    PREPROCCESOR_DIRECTIVE : DEFINE 
                            | INCLUDE
    """


def p_DEFINE(p):
    """
    DEFINE : PP_DEFINE VARIABLELEX VALUE
    
    """
    p[0] = ('DEFINE', p[1])

def p_INCLUDE(p):
    """
    INCLUDE : PP_INCLUDE HEADER_LIB
    """
    p[0] = ('INCLUDE', p[1])


def p_VALUE(p):
    """
    VALUE : NUMBER 
            | STRING
    """

def p_NUMBER(p):
    """
    NUMBER : INTEGER
            | DECIMAL
    """ 
    p[0] = ('NUMBER', p[1])


def p_SENTENCIAS(p):
    """
    SENTENCIAS : IF
                | ELSEIF
                | ELSE
                | FOR
                | WHILE
                | SWITCH
    """
    p[0] = ('SENTENCIAS', p[1])


def p_DATA_TYPE(p):
    """
    DATA_TYPE : INTEGER_TYPE
            | DECIMAL_TYPE
            | CHAR
    """
    p[0] = ('DATA_TYPE', p[1])


def p_INTEGER_TYPE(p):
    """
    INTEGER_TYPE : INT
                | SHORT
                | LONG
    """
    p[0] = ('INTEGER_TYPE', p[1])


def p_DECIMAL_TYPE(p):
    """
    DECIMAL_TYPE : FLOAT
                | DOUBLE
    """
    p[0] = ('DECIMAL_TYPE', p[1])


def p_DECLARATION(p):
    """
    DECLARATION : DATA_TYPE VARNAME EQUAL INTEGER
    """
    p[0] = ('DECLARATION', p[1])


def p_INTEGER_DECLARATION(p):
    """
    INTEGER_DECLARATION : INTEGER_TYPE VARNAME EQUAL INTEGER
    """
    p[0] = ('INTEGER_DECLARATION', p[1])


def p_DECIMAL_DECLARATION(p):
    """
    DECIMAL_DECLARATION : DECIMAL_TYPE VARNAME EQUAL DECIMAL
    """
    p[0] = ('DECIMAL_DECLARATION', p[1])

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
    OPERATION : NUMBER OPERADOR NUMBER
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

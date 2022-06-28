from lexical import tokens
import ply.yacc as yacc


def p_EXPRESSION(p):
    """
    EXPRESSION : COMENTARIOLEX
                | VARIABLELEX
                | SUMA
    """
    p[0] = ('EXPRESSION', p[1])


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


def p_SUMA(p):
    """
    SUMA : INTEGER OPERADOR INTEGER
    """
    p[0] = ('SUMA', p[1])


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
    result = parser.parse(data)
    return result

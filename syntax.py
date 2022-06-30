from lexicon import tokens
import ply.yacc as yacc


def p_EXPRESSION(p):
    """
    EXPRESSION : COMENTARIOLEX
                | VARIABLELEX 
                | OPERATION
                | OPERATIONS
                | OPERATOR
                | SENTENCIAS
                | INCLUDE
                | DEFINE
                | PREPROCESOR_DIRECTIVE
                | LOGICAL_OPERATOR
                | COMPARISONS
                | COMPARISON
                | COMPARISON_OPERATOR
                | DECIMAL_DECLARATION
                | INTEGER_DECLARATION
                | DECIMAL_TYPE
                | INTEGER_TYPE
                | ASSIGNMENT_DECLARATION
                | ASSIGNMENT_OPERATOR

    """
    p[0] = ('EXPRESSION', p[1])


# START GABRIELA RAMOS
def p_PREPROCESOR_DIRECTIVE(p):
    """
    PREPROCESOR_DIRECTIVE : DEFINE
                            | INCLUDE
    """
    p[0] = ('PREPROCESOR_DIRECTIVE', p[1])


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
    p[0] = ('VALUE', p[1])


def p_NUMBER(p):
    """
    NUMBER : INTEGER
            | DECIMAL
    """ 
    p[0] = ('NUMBER', p[1])


def p_CONTROL_STRUCTURES(p):
    """
    CONTROL_STRUCTURES : IF_STRUCTURE
                        | FOR_STRUCTURE
                        | WHILE_STRUCTURE
                        | SWITCH_STRUCTURE
    """
    p[0] = ('CONTROL_STRUCTURES', p[1])


# END GABRIELA RAMOS

# START PAUL SORIA

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


def p_ASSIGNMENT_DECLARATION(p):
    """
    ASSIGNMENT_DECLARATION : VARNAME ASSIGNMENT_OPERATOR SENTENCE
    """
    p[0] = ('ASSIGNMENT_DECLARATION', p[1])


def p_ASSIGNMENT_OPERATOR(p):
    """
    ASSIGNMENT_OPERATOR : EQUAL
                        | PLUS_EQUAL
                        | MINUS_EQUAL
                        | DIV_EQUAL
                        | TIMES_EQUAL
                        | MOD_EQUAL
                        | AND_EQUAL
                        | OR_EQUAL
                        | XOR_EQUAL
                        | COMPLEMENT_EQUAL
                        | SHIFTL_EQUAL
                        | SHIFTR_EQUAL
    """
    p[0] = ('ASSIGNMENT_OPERATOR', p[1])


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


def p_OPERATOR(p):
    """
    OPERATOR : PLUS
              | MINUS
              | TIMES
              | MODULUS
              | DIVIDE
    """
    p[0] = ('OPERATOR', p[1])


def p_OPERATION(p):
    """
    OPERATION : NUMBER OPERATOR NUMBER
    """
    p[0] = ('OPERATION', p[1])


def p_OPERATIONS(p):
    """
    OPERATIONS : OPERATION
                | OPERATION OPERATOR OPERATIONS
    """
    p[0] = ('OPERATIONS', p[1])


def p_COMPARISON_OPERATOR(p):
    """
    COMPARISON_OPERATOR : EQUAL_TO
                        | NOT_EQUAL
                        | GREATER_THAN
                        | LESS_THAN
                        | GREATER_EQUAL
                        | LESS_EQUAL
    """
    p[0] = ('COMPARISON_OPERATOR', p[1])


def p_COMPARISON(p):
    """
    COMPARISON : VALUE COMPARISON_OPERATOR VALUE
    """
    p[0] = ('COMPARISON', p[1])


def p_COMPARISONS(p):
    """
    COMPARISONS : COMPARISON
                | COMPARISON LOGICAL_OPERATOR COMPARISONS
    """
    p[0] = ('COMPARISONS', p[1])


def p_LOGICAL_OPERATOR(p):
    """
    LOGICAL_OPERATOR : AND
                    | OR
                    | NOT
    """
    p[0] = ('LOGICAL_OPERATOR', p[1])


def p_SENTENCE(p):
    """
    SENTENCE : NUMBER
            | VARNAME
    """
    p[0] = ('SENTENCE', p[1])

# END PAUL SORIA


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

from analyzers.lexicon import tokens
import ply.yacc as yacc


def p_ROOT(p):
    """
    ROOT : PREPROCESOR_DIRECTIVE
         | DEFINE
         | INCLUDE
         | VALUE
         | NUMBER
         | CONTROL_STRUCTURES
         | WHILE_STRUCTURE
         | SWITCH_STRUCTURE
         | IF_STRUCTURE
         | FOR_STRUCTURE
         | CODE
         | EXPRESSION
         | EXPRESSIONS
         | FUNCTION
         | INTEGER_TYPE
         | DECIMAL_TYPE
         | INTEGER_DECLARATION
         | DECIMAL_DECLARATION
         | CHARACTER_DECLARATION
         | ASSIGNMENT_DECLARATION
         | ASSIGNMENT_OPERATOR
         | COMENTARIOLEX
         | VARIABLELEX
         | OPERATOR
         | OPERATION
         | OPERATIONS
         | COMPARISON_OPERATOR
         | COMPARISON
         | COMPARISONS
         | LOGICAL_OPERATOR
         | STATEMENT
         | SWITCH_BODY
         | BUCLE
         | ELSE_STRUCTURE
         | FUNCTION_ARGUMENTS
         | DECLARATIONS
         | SKIP_STRUCTURE
         | FOR_ARGUMENTS_STRUCTURE
         | INCREMENTS
         | DECREMENTS
         | FUNCTION_PROTOTYPE
         | VALUES
         | PARAMETERS
         | RETURN_STATEMENT
         | RETURN_TYPE
         | BITWISE_OPERATOR
         | BITWISE_OPERATIONS
         | MATH_OPERATION
         | INTEGER_OPERATION
         | INTEGER_OPERATIONS
         | DECIMAL_OPERATION
         | DECIMAL_OPERATIONS
         | MATH_OPERATIONS
         | TYPEDEF_INTEGER
         | TYPEDEF_DECIMAL
         | TYPEDEF_CHAR
         | TYPEDEF_STRUCT
         | ARRAY_DECLARATION_INTEGER
         | ARRAY_DECLARATION_DECIMAL
         | ARRAY_DECLARATION_CHAR
         | ARRAY_DECLARATION_INTEGER_ASSIGNMENT
         | ARRAY_DECLARATION_DECIMAL_ASSIGNMENT
         | ARRAY_DECLARATIONS
         | ARRAY_ASSIGNMENTS
         | INTEGERS
         | DECIMALS
         | CHARACTERS
         | ARRAY_DECLARATION
    """
    p[0] = ('ROOT', p[1])


def p_ARRAY_DECLARATION_INTEGER(p):
    """
    ARRAY_DECLARATION_INTEGER : INTEGER_TYPE ARRAY_DECLARATION
    """
    p[0] = ('ARRAY_DECLARATION_INTEGER', p[1])


def p_ARRAY_DECLARATION_DECIMAL(p):
    """
    ARRAY_DECLARATION_DECIMAL : DECIMAL_TYPE ARRAY_DECLARATION
    """
    p[0] = ('ARRAY_DECLARATION_DECIMAL', p[1])


def p_ARRAY_DECLARATION_CHAR(p):
    """
    ARRAY_DECLARATION_CHAR : CHAR ARRAY_DECLARATION
    """
    p[0] = ('ARRAY_DECLARATION_CHAR', p[1])


def p_ARRAY_DECLARATION(p):
    """
    ARRAY_DECLARATION : VARNAME LBRACKET INTEGER RBRACKET
    """
    p[0] = ('ARRAY_DECLARATION', p[1])

def p_ARRAY_DECLARATION_INTEGER_ASSIGNMENT(p):
    """
    ARRAY_DECLARATION_INTEGER_ASSIGNMENT : ARRAY_DECLARATION_INTEGER EQUAL LBRACKET INTEGERS RBRACKET
    """
    p[0] = ('ARRAY_DECLARATION_INTEGER_ASSIGNMENT', p[1])


def p_ARRAY_DECLARATION_DECIMAL_ASSIGNMENT(p):
    """
    ARRAY_DECLARATION_DECIMAL_ASSIGNMENT : ARRAY_DECLARATION_DECIMAL EQUAL LBRACKET DECIMALS RBRACKET
    """
    p[0] = ('ARRAY_DECLARATION_DECIMAL_ASSIGNMENT', p[1])

'''
def p_ARRAY_DECLARATION_CHAR_ASSIGNMENT(p):
    """
    ARRAY_DECLARATION_CHAR_ASSIGNMENT : ARRAY_DECLARATION_CHAR EQUAL LBRACKET CHARARCTERS RBRACKET
    """
    p[0] = ('ARRAY_DECLARATION_CHAR_ASSIGNMENT', p[1])
'''

def p_ARRAY_DECLARATIONS(p):
    """
    ARRAY_DECLARATIONS : ARRAY_DECLARATION_INTEGER
                        | ARRAY_DECLARATION_DECIMAL
                        | ARRAY_DECLARATION_CHAR
    """
    p[0] = ('ARRAY_DECLARATIONS', p[1])


def p_ARRAY_ASSIGNMENTS(p):
    """
    ARRAY_ASSIGNMENTS : ARRAY_DECLARATION_INTEGER_ASSIGNMENT
                        | ARRAY_DECLARATION_DECIMAL_ASSIGNMENT
    """
    p[0] = ('ARRAY_ASSIGNMENTS', p[1])


def p_INTEGERS(p):
    """
    INTEGERS : INTEGER
             | INTEGER COMMA INTEGERS
    """
    p[0] = ('INTEGERS', p[1])


def p_CHARACTERS(p):
    """
    CHARACTERS : CHARACTER
             | CHARACTER COMMA CHARACTERS
    """
    p[0] = ('CHARACTERS', p[1])


def p_DECIMALS(p):
    """
    DECIMALS : DECIMAL
             | DECIMAL COMMA DECIMALS
    """
    p[0] = ('DECIMALS', p[1])


def p_TYPEDEF_STRUCT(p):
    """
    TYPEDEF_STRUCT : TYPEDEF_INTEGER
            | TYPEDEF_DECIMAL
            | TYPEDEF_CHAR
    """
    p[0] = ('TYPEDEF_STRUCT', p[1])


def p_TYPEDEF_INTEGER(p):
    """
    TYPEDEF_INTEGER : TYPEDEF INTEGER_TYPE VARNAME LBRACKET INTEGER RBRACKET
    """
    p[0] = ('TYPEDEF_INTEGER', p[1])


def p_TYPEDEF_DECIMAL(p):
    """
    TYPEDEF_DECIMAL : TYPEDEF DECIMAL_TYPE VARNAME LBRACKET INTEGER RBRACKET
    """
    p[0] = ('TYPEDEF_DECIMAL', p[1])


def p_TYPEDEF_CHAR(p):
    """
    TYPEDEF_CHAR : TYPEDEF CHAR VARNAME LBRACKET INTEGER RBRACKET
    """
    p[0] = ('TYPEDEF_CHAR', p[1])


def p_INCREMENTS(p):
    """
    INCREMENTS : VARNAME INCREASE
    """
    p[0] = ('INCREMENTS', p[1])


def p_DECREMENTS(p):
    """
    DECREMENTS : VARNAME DECREASE
    """
    p[0] = ('DECREMENTS', p[1])


def p_UNDEF(p):
    """
    UNDEF : PP_UNDEF VARNAME
    """
    p[0] = ('UNDEF', p[1])


def p_BITWISE_OPERATIONS(p):
    """
    BITWISE_OPERATIONS : STATEMENT BITWISE_OPERATOR STATEMENT
    """
    p[0] = ('BITWISE_OPERATIONS', p[1])


def p_BITWISE_OPERATOR(p):
    """
    BITWISE_OPERATOR : B_AND
                     | B_OR
                     | B_XOR
                     | B_COMPLEMENT
                     | SHIFT_LEFT
                     | SHIFT_RIGHT
    """
    p[0] = ('BITWISE_OPERATOR', p[1])


# <---------- START GABRIELA RAMOS ---------->
def p_PREPROCESOR_DIRECTIVE(p):
    """
    PREPROCESOR_DIRECTIVE : DEFINE
                          | INCLUDE
                          | UNDEF
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
          | CHARACTER
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


def p_BODY_STRUCTURE(p):
    """
    BODY_STRUCTURE : EXPRESSIONS 
                   | EXPRESSIONS BREAK SEMICOLON
                   | EXPRESSIONS CONTINUE SEMICOLON
    """
    p[0] = ('BODY_STRUCTURE', p[1])

# WHILE STATEMENT


def p_WHILE_STRUCTURE(p):
    """
    WHILE_STRUCTURE : WHILE LPAREN COMPARISONS RPAREN LCURL_BRACE BODY_STRUCTURE RCURL_BRACE
    """
    p[0] = ('WHILE_STRUCTURE', p[1])

# SWITCH STATEMENT


def p_SWITCH_CASE(p):
    """
    SWITCH_CASE : CASE INTEGER COLON EXPRESSIONS BREAK SEMICOLON
                | CASE VARNAME COLON EXPRESSIONS BREAK SEMICOLON
                | CASE STRING COLON EXPRESSIONS BREAK SEMICOLON
    """
    p[0] = ('SWITCH_CASE', p[1])


def p_SWITCH_DEFAULT(p):
    """
    SWITCH_DEFAULT : DEFAULT COLON EXPRESSIONS BREAK SEMICOLON
    """
    p[0] = ('SWITCH_DEFAULT', p[1])


def p_SWITCH_BODY(p):
    """
    SWITCH_BODY : SWITCH_CASE
                | SWITCH_DEFAULT
                |  SWITCH_CASE SWITCH_BODY   
    """
    p[0] = ('SWITCH_BODY', p[1])


def p_SWITCH_STRUCTURE(p):
    """
    SWITCH_STRUCTURE : SWITCH LPAREN VARNAME RPAREN LCURL_BRACE SWITCH_BODY RCURL_BRACE
    """
    p[0] = ('SWITCH_STRUCTURE', p[1])


# FOR STATEMENT

def p_BUCLE(p):
    """
    BUCLE : VARIABLELEX INCREASE 
          | DECREASE VARIABLELEX
    """
    p[0] = ('BUCLE', p[1])


# FOR LPAREN EXPRESSIONS COMPARISONS BUCLE RPAREN
def p_FOR_STRUCTURE(p):
    """
    FOR_STRUCTURE : FOR FOR_ARGUMENTS_STRUCTURE LCURL_BRACE SKIP_STRUCTURE RCURL_BRACE
    """
    p[0] = ('FOR_STRUCTURE', p[1])


def p_FOR_ARGUMENTS_STRUCTURE(p):
    """
    FOR_ARGUMENTS_STRUCTURE : LPAREN DECLARATIONS SEMICOLON COMPARISONS SEMICOLON BUCLE RPAREN
    """
    p[0] = ('FOR_ARGUMENTS_STRUCTURE', p[1])


def p_SKIP_STRUCTURE(p):
    """
    SKIP_STRUCTURE : EXPRESSIONS
                       | BREAK SEMICOLON
                       | CONTINUE SEMICOLON
    """
    p[0] = ('SKIP_STRUCTURE', p[1])

# <---------- END GABRIELA RAMOS ---------->


# <----------- START PAUL SORIA ---------->

# IF STATEMENT

def p_IF_STRUCTURE(p):
    """
    IF_STRUCTURE : IF LPAREN COMPARISONS RPAREN LCURL_BRACE EXPRESSIONS RCURL_BRACE
                 | IF LPAREN COMPARISONS RPAREN LCURL_BRACE EXPRESSIONS RCURL_BRACE ELSE_STRUCTURE
    """
    p[0] = ('IF_STRUCTURE', p[1])


def p_ELSE_STRUCTURE(p):
    """
    ELSE_STRUCTURE : ELSE LCURL_BRACE EXPRESSIONS RCURL_BRACE
                   | ELSE IF_STRUCTURE
    """
    p[0] = ('ELSE_STRUCTURE', p[1])


def p_DECLARATIONS(p):
    """
    DECLARATIONS : INTEGER_DECLARATION
                 | DECIMAL_DECLARATION
                 | CHARACTER_DECLARATION
    """
    p[0] = ('DECLARATIONS', p[1])


def p_CODE(p):
    """
    CODE : FUNCTION
         | INTEGER_DECLARATION
         | DECIMAL_DECLARATION
         | CHARACTER_DECLARATION
         | ASSIGNMENT_DECLARATION
         | INCREMENTS
         | DECREMENTS
         | TYPEDEF_STRUCT
         | ARRAY_DECLARATIONS
         | ARRAY_ASSIGNMENTS
         | ARRAY_DECLARATION
    """
    p[0] = ('CODE', p[1])


def p_EXPRESSION(p):
    """
    EXPRESSION : CODE SEMICOLON
               | CONTROL_STRUCTURES
               | COMENTARIOLEX
    """
    p[0] = ('EXPRESSION', p[1])


def p_EXPRESSIONS(p):
    """
    EXPRESSIONS : EXPRESSION
                | EXPRESSION EXPRESSIONS
    """
    p[0] = ('EXPRESSIONS', p[1])


def p_FUNCTION(p):
    """
    FUNCTION : VARNAME LPAREN FUNCTION_ARGUMENTS RPAREN
    """
    p[0] = ('FUNCTION', p[1])


def p_FUNCTION_ARGUMENTS(p):
    """
    FUNCTION_ARGUMENTS : STATEMENTS
                       | COMPARISONS
    """
    p[0] = ('FUNCTION_ARGUMENTS', p[1])


def p_INTEGER_TYPE(p):
    """
    INTEGER_TYPE : INT
                 | SHORT
                 | LONG
                 | CHAR
    """
    p[0] = ('INTEGER_TYPE', p[1])


def p_DECIMAL_TYPE(p):
    """
    DECIMAL_TYPE : FLOAT
                 | DOUBLE
    """
    p[0] = ('DECIMAL_TYPE', p[1])


def p_INTEGER_VALUE(p):
    """
    INTEGER_VALUE : INTEGER
                  | INTEGER_OPERATIONS
    """
    p[0] = ('INTEGER_VALUE', p[1])


def p_INTEGER_DECLARATION(p):
    """
    INTEGER_DECLARATION : INTEGER_TYPE VARNAME EQUAL INTEGER_VALUE
    """
    p[0] = ('INTEGER_DECLARATION', p[1])


def p_DECIMAL_VALUE(p):
    """
    DECIMAL_VALUE : DECIMAL
                  | DECIMAL_OPERATIONS
    """
    p[0] = ('DECIMAL_VALUE', p[1])


def p_DECIMAL_DECLARATION(p):
    """
    DECIMAL_DECLARATION : DECIMAL_TYPE VARNAME EQUAL DECIMAL_VALUE
    """
    p[0] = ('DECIMAL_DECLARATION', p[1])


def p_CHARACTER_DECLARATION(p):
    """
    CHARACTER_DECLARATION : CHAR VARNAME EQUAL CHARACTER
    """
    p[0] = ('CHARACTER_DECLARATION', p[1])


def p_ASSIGNMENT_DECLARATION(p):
    """
    ASSIGNMENT_DECLARATION : VARNAME ASSIGNMENT_OPERATOR STATEMENT
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


def p_MATH_OPERATION(p):
    """
    MATH_OPERATION : NUMBER OPERATOR NUMBER
    """
    p[0] = ('MATH_OPERATION', p[1])


def p_MATH_OPERATIONS(p):
    """
    MATH_OPERATIONS : MATH_OPERATION
                    | MATH_OPERATION OPERATOR MATH_OPERATIONS
    """
    p[0] = ('MATH_OPERATIONS', p[1])


def p_INTEGER_OPERATION(p):
    """
    INTEGER_OPERATION : INTEGER OPERATOR INTEGER
    """
    p[0] = ('INTEGER_OPERATION', p[1])


def p_INTEGER_OPERATIONS(p):
    """
    INTEGER_OPERATIONS : INTEGER_OPERATION
                       | INTEGER_OPERATION OPERATOR INTEGER_OPERATIONS
    """
    p[0] = ('INTEGER_OPERATIONS', p[1])


def p_DECIMAL_OPERATION(p):
    """
    DECIMAL_OPERATION : DECIMAL OPERATOR DECIMAL
    """
    p[0] = ('DECIMAL_OPERATION', p[1])


def p_DECIMAL_OPERATIONS(p):
    """
    DECIMAL_OPERATIONS : DECIMAL_OPERATION
                       | DECIMAL_OPERATION OPERATOR DECIMAL_OPERATIONS
    """
    p[0] = ('DECIMAL_OPERATIONS', p[1])


def p_OPERATION(p):
    """
    OPERATION : MATH_OPERATION
              | BITWISE_OPERATIONS
              | INTEGER_OPERATION
              | DECIMAL_OPERATION
              | MATH_OPERATIONS
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
               | STATEMENT COMPARISON_OPERATOR STATEMENT
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


def p_STATEMENT(p):
    """
    STATEMENT : NUMBER
             | VARNAME
             | OPERATIONS
    """
    p[0] = ('STATEMENT', p[1])


def p_STATEMENTS(p):
    """
    STATEMENTS : STATEMENT
               | STATEMENT COMMA STATEMENTS
    """
    p[0] = ('STATEMENTS', p[1])

# <---------- END PAUL SORIA ---------->


# <---------- START JUAN PITA---------->

def p_VALUES(p):
    """
    VALUES : VALUE
           | VALUE COMMA VALUES
    """
    p[0] = ('VALUES', p[1])


def p_RETURN_TYPE(p):
    """
    RETURN_TYPE : INTEGER_TYPE
                | DECIMAL_TYPE
                | VOID
    """
    p[0] = ('RETURN_TYPE', p[1])


def p_RETURN_STATEMENT(p):
    """
    RETURN_STATEMENT : RETURN PARAMETERS SEMICOLON
                     | RETURN VALUES SEMICOLON
    """
    p[0] = ('RETURN_STATEMENT', p[1])


def p_PARAMETERS(p):
    """
    PARAMETERS : VARNAME 
               | VARNAME COMMA PARAMETERS
    """
    p[0] = ('PARAMETERS', p[1])


def p_FUNCTION_PROTOTYPE(p):
    """
    FUNCTION_PROTOTYPE : RETURN_TYPE VARNAME LPAREN RPAREN LCURL_BRACE EXPRESSIONS RETURN_STATEMENT RCURL_BRACE
                       | RETURN_TYPE VARNAME LPAREN PARAMETERS RPAREN LCURL_BRACE EXPRESSIONS RETURN_STATEMENT RCURL_BRACE
    """
    p[0] = ('FUNCTION_PROTOTYPE', p[1])

# <---------- END JUAN PITA ---------->


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
        return result


def syntax_analyzer(data):
    return parser.parse(data)


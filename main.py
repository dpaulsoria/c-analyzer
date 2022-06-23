import ply.lex as lexical

# List of key/reserved words

reserved = {
    # Control Structures
    "if": "IF",
    "else if": "ELSEIF",
    "else": "ELSE",
    "switch": "SWITCH",
    "case": "CASE",
    "break": "BREAK",
    "continue": "CONTINUE",
    "default": "DEFAULT",
    "return": "RETURN",

    # Loop Structures
    "for": "FOR",
    "while": "WHILE",
    "do": "DO",

    # Control flow
    "goto": "GOTO",

    # Data Types
    "void": "VOID",
    "char": "CHAR",
    "short": "SHORT",
    "int": "INT",
    "long": "LONG",
    "float": "FLOAT",
    "double": "DOUBLE",
    "struct": "STRUCT",
    "typedef": "TYPEDEF",
    "enum": "ENUM",
    "union": "UNION",

    # Data Type Properties
    "unsigned": "UNSIGNED",
    "signed": "SIGNED",
    "const": "CONST",
    "voltile": "VOLTILE",

    # Storage Classes
    'auto': 'AUTO',
    "extern": "EXTERN",
    "register": "REGISTER",
    "static": "STATIC",

    # Unary Operators
    "sizeof": "SIZEOF",
}

# List of token names

tokens = (
    # Arithmetic Operators
    'PLUS',  # +
    'MINUS',  # -
    'TIMES',  # *
    'DIVIDE',  # /
    'MODULUS',  # %

    # Arithmetic Assignment Operators
    'EQUAL',  # =
    'PLUS_EQUAL',  # +=
    'MINUS_EQUAL',  # -=
    'TIMES_EQUAL',  # *=
    'DIV_EQUAL',  # /=
    'MOD_EQUAL',  # %=

    # Bitwise Assignment Operators
    'AND_EQUAL',  # &=
    'OR_EQUAL',  # |=
    'XOR_EQUAL',  # ^=
    'COMPLEMENT_EQUAL',  # ~=
    'SHIFTL_EQUAL',  # <<=
    'SHIFTR_EQUAL',  # >>=

    # Comparison Operators
    'EQUAL_TO',  # ==
    'NOT_EQUAL',  # !=
    'GREATER_THAN',  # >
    'LESS_THAN',  # <
    'GREATER_EQUAL',  # >=
    'LESS_EQUAL',  # <=

    # Logical Operators
    'AND',  # &&
    'OR',  # ||
    'NOT',  # !

    # Bitwise Operators
    'B_AND',  # &
    'B_OR',  # |
    'B_XOR',  # ^
    'B_COMPLEMENT',  # ~
    'SHIFT_LEFT',  # <<
    'SHIFT_RIGHT',  # >>

    # Groups
    'LPAREN',  # (
    'RPAREN',  # )
    'LBRACKET',  # [
    'RBRACKET',  # ]
    'LCURL_BRACE',  # {
    'RCURL_BRACE',  # }

    # Values
    'VARNAME',  # Variables
    'INTEGER',
    'DECIMAL',
    'CHARACTER',
    'STRING',

    # Miscellaneous
    'SINGLE_QUOTE',
    'DOUBLE_QUOTE',
    'COLON',  # :
    'SEMICOLON',  # ;
    'DOT',  # .
    'COMMA',  # ,
    'QUESTIONMARK',  # ?
    'AMPERSAND',  # &
    'TILDE',  # ~
    'COMMENT',  # // y /** */
    'IGNORE',

    # Preprocessor Directives
    'PP_INCLUDE',  # #include
    'PP_DEFINE',  # #define
    'PP_UNDEF',  # #undef
    'PP_IF',  # #if
    'PP_IFDEF',  # #ifdef
    'PP_IFNDEF',  # #ifndef
    'PP_ERROR',  # error
    'PP_PRAGMA',  # pragma
    # Preprocessor Macros
    'PP_FILE',  # __FILE__
    'PP_LINE',  # __LINE__
    'PP_DATE',  # __DATE__
    'PP_TIME',  # __TIME__
    'PP_TIMESTAMP',  # __TIMESTAMP__
    'PP_STMACRO',  # # single token macro
    'PP_DTMACRO',  # ## double token macro
    'HEADER_LIB',  # <stdio.h> || "lib.h"

    # Format specifiers
    'FS_CHAR',  # %c
    'FS_INT',  # %d | %i
    'FS_LONG',  # %ld | %D
    'FS_FLOAT',  # %f
    'FS_SCI_NOTATION',  # %e | %E | %g | %G
    'FS_STRING',  # %s
    'FS_UNSIGNED_INT',  # %u
    'FS_UNSIGNED_LONG',  # %lu | %U
    'FS_OCT',  # %o
    'FS_HEX',  # %x | %X
    'FS_POINTER',  # %p
    'FS_OCT_LONG',  # %lo | %O
    'FS_DOUBLE',  # %lf
    'FS_LONG_DOUBLE',  # %LF

    # Secuencias de escape
    'NEWLINE',  # \n
    'BACKSPACE',  # \b
    'HTAB',  # \t
    'VTAB',  # \v
    'BACKSLASH',  # \\
    'FF_PAGEBREAK',  # \f
    'SINGLE_APOS',  # \'
    'DOUBLE_APOS',  # \"
    'NULL',  # \0 end of line
) + tuple(reserved.values())


def t_lineCounter(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_COMMENT(t):
    # r'\/\/.*|\/\*\*\s.*\s\*\/'
    r'\/\/.*|\/\*(\*(?!\/)|[^*])*\*\/'
    t.type = reserved.get(t.value, "COMMENT")
    return t


def t_error(t):
    print(f"    ¡ALERT! Unknown character --> {t.value[0]} <-- in line {t.lineno}")
    t.lexer.skip(1)


validador = lexical.lex()


def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


line = " "
code = open("test/little.c")
for line in code:
    validador.input(line)
    getTokens(validador)
code.close()

# print(f"Number of unknowns {errors}")
print("End... :)")

# -*- coding: utf-8 -*-
import re

import ply.lex as lexical

# START PAUL SORIA

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

# END PAUL SORIA

# START JUAN PITA

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
    'HEADER_LIB',  # stdio.h || lib.h

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

# END JUAN PITA

# START GABRIELA RAMOS

# Regular expression rules for simple tokens

# Arithmetic Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_MODULUS = r'%'

# Assignment Operators
t_EQUAL = r'='
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_TIMES_EQUAL = r'\*='
t_DIV_EQUAL = r'\/='
t_MOD_EQUAL = r'\%='

# Bitwise Assignment Operators
t_AND_EQUAL = r'\&='
t_OR_EQUAL = r'\|='
t_XOR_EQUAL = r'\^='
t_COMPLEMENT_EQUAL = r'\~='
t_SHIFTL_EQUAL = r'\<\<\='
t_SHIFTR_EQUAL = r'\>\>\='

# Comparison Operators
t_EQUAL_TO = r'=='
t_NOT_EQUAL = r'!='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='

# Logical Operators
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'\!'

# Bitwise Operators
t_B_AND = r'\&'
t_B_OR = r'\|'
t_B_XOR = r'\^'
t_B_COMPLEMENT = r'\~'
t_SHIFT_LEFT = r'\<\<'
t_SHIFT_RIGHT = r'\>\>'

# Groups
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURL_BRACE = r'\{'
t_RCURL_BRACE = r'\}'

# Values
t_VARNAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_INTEGER = r'[0-9]+'
t_DECIMAL = r'[0-9]*\.[0-9]+'
t_CHARACTER = r'\'\w+\''
# t_STRING = r'\".*\"'

# Miscellaneous
t_SINGLE_QUOTE = r'\''
t_DOUBLE_QUOTE = r'\"'
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_DOT = r'\.'
t_COMMA = r'\,'
t_QUESTIONMARK = r'\?'
t_AMPERSAND = r'\&'
t_TILDE = r'\~'
# t_COMMENT = r'\/\/.*|\/\*(\*(?!\/)|[^*])*\*\/'
t_ignore = " \t"

# Preprocessor Directives
t_PP_INCLUDE = r'\#include'
t_PP_DEFINE = r'\#define'
t_PP_UNDEF = r'\#undef'
t_PP_IF = r'\#if'
t_PP_IFDEF = r'\#ifdef'
t_PP_IFNDEF = r'\#ifndef'
t_PP_ERROR = r'\#error'
t_PP_PRAGMA = r'\#pragma'
# Preprocessor Macros
t_PP_FILE = r'__FILE__'
t_PP_LINE = r'__LINE__'
t_PP_DATE = r'__DATE__'
t_PP_TIME = r'__TIME__'
t_PP_TIMESTAMP = r'__TIMESTAMP__'

# t_PP_STMACRO = r'\S+\s\S+'  # Single token Macro
# t_PP_DTMACRO = r'\#\S+\s.+'  # Double token Macro

t_HEADER_LIB = r'<[a-z\_\/]+\.h>|\"[a-z\_\/]+\.h\"'

# Format specifiers
t_FS_CHAR = r'%c'
t_FS_INT = r'%d|%i'
t_FS_LONG = r'%ld|%D'
t_FS_FLOAT = r'%f'
t_FS_SCI_NOTATION = r'%e|%E|%g|%G'
t_FS_STRING = r'%s'
t_FS_UNSIGNED_INT = r'%u'
t_FS_UNSIGNED_LONG = r'%lu|%U'
t_FS_OCT = r'%o'
t_FS_HEX = r'%x|%X'
t_FS_POINTER = r'%p'
t_FS_OCT_LONG = r'%lo|%O'
t_FS_DOUBLE = r'%lf'
t_FS_LONG_DOUBLE = r'%LF'

# Secuencias de escape
t_NEWLINE = r'\\n'
t_BACKSPACE = r'\\b'
t_HTAB = r'\\t'
t_VTAB = r'\\v'
t_BACKSLASH = r'\\\\'
t_FF_PAGEBREAK = r'\\f'  # Formfeed Page Break
t_SINGLE_APOS = r'\\\''
t_DOUBLE_APOS = r'\\\"'
t_NULL = r'\\0'  # end of line or null


# END GABRIELA RAMOS


def t_lineCounter(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count("\n")


# START GABRIELA RAMOS


def t_COMMENT(t):
    # r'\/\/.*|\/\*\*\s.*\s\*\/'
    r"""\/\/.*|\/\*(\*(?!\/)|[^*])*\*\/"""
    t.type = reserved.get(t.value, "COMMENT")
    return t


# END GABRIELA RAMOS

# START JUAN PITA


def t_VARIABLE(t):
    r"""[a-zA-Z_][a-zA-Z0-9_]*"""
    t.type = reserved.get(t.value, "VARNAME")
    return t


# END JUAN PITA

# START PAUL SORIA


def t_STRING(t):
    r"""\"[^<[a-z\_\/]+\.h>|\"[a-z\_\/]+\.h\"].*\""""

    result_specifier = verify_format_spec(t.value[1:-1])
    if result_specifier[0]:
        t.type = reserved.get(t.value, result_specifier[1])
    else:
        t.type = reserved.get(t.value, 'STRING')
    return t


def verify_format_spec(value):
    if bool(re.match(value, t_FS_CHAR)):
        return True, 'FS_CHAR'
    elif bool(re.match(value, t_FS_INT)):
        return True, 'FS_INT'
    elif bool(re.match(value, t_FS_LONG)):
        return True, 'FS_LONG'
    elif bool(re.match(value, t_FS_SCI_NOTATION)):
        return True, 'FS_SCI_NOTATION'
    elif bool(re.match(value, t_FS_STRING)):
        return True, 'FS_STRING'
    elif bool(re.match(value, t_FS_UNSIGNED_INT)):
        return True, 'FS_UNSIGNED_INT'
    elif bool(re.match(value, t_FS_UNSIGNED_LONG)):
        return True, 'FS_UNSIGNED_LONG'
    elif bool(re.match(value, t_FS_OCT)):
        return True, 'FS_OCT'
    elif bool(re.match(value, t_FS_HEX)):
        return True, 'FS_HEX'
    elif bool(re.match(value, t_FS_POINTER)):
        return True, 'FS_POINTER'
    elif bool(re.match(value, t_FS_OCT_LONG)):
        return True, 'FS_OCT_LONG'
    elif bool(re.match(value, t_FS_DOUBLE)):
        return True, 'FS_DOUBLE'
    elif bool(re.match(value, t_FS_LONG_DOUBLE)):
        return True, 'FS_LONG_DOUBLE'
    else:
        return False, None


# END PAUL SORIA


def t_error(t):
    print(f"    ¡ALERT! Unknown character {t.value[0]} in line {t.lineno}")
    t.lexer.skip(1)


validator = lexical.lex()


def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


line = " "
code = open("tests/keylogger.c")
for line in code:
    # print(">>>", line, len(line))
    # print(type(line))
    # print(bool(re.match(line, r'\t')))
    validator.input(line)
    getTokens(validator)
code.close()

print("End... :)")

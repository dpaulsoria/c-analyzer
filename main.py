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


def p_sentences_include(p):
  'include : PP_INCLUDE HEADER_LIB'
  
def p_sentencias(p):
  'sentencias : VAR_NAME'

def p_valor(p):
  '''valor : VAR_NAME
            | INTEGER
            | DECIMAL
            | SINGLE_QUOTE 
            | DOUBLE_QUOTE'''

def p_valores(p):
  '''valores : valor 
              | valor COLON valores'''

def p_operator(p):
  '''operator : PLUS
              | MINUS 
              | TIMES 
              | MODULUS 
              | DIVIDE'''

def p_impresion(p):
  'impresion : PRINTF LPAREN valores COLON VAR_NAME  RPAREN'
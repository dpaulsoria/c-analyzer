
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND AND AND_EQUAL AUTO BACKSLASH BACKSPACE BREAK B_AND B_COMPLEMENT B_OR B_XOR CASE CHAR CHARACTER COLON COMMA COMMENT COMPLEMENT_EQUAL CONST CONTINUE DECIMAL DEFAULT DIVIDE DIV_EQUAL DO DOT DOUBLE DOUBLE_APOS DOUBLE_QUOTE ELSE ELSEIF ENUM EQUAL EQUAL_TO EXTERN FF_PAGEBREAK FLOAT FOR FS_CHAR FS_DOUBLE FS_FLOAT FS_HEX FS_INT FS_LONG FS_LONG_DOUBLE FS_OCT FS_OCT_LONG FS_POINTER FS_SCI_NOTATION FS_STRING FS_UNSIGNED_INT FS_UNSIGNED_LONG GOTO GREATER_EQUAL GREATER_THAN HEADER_LIB HTAB IF IGNORE INT INTEGER LBRACKET LCURL_BRACE LESS_EQUAL LESS_THAN LONG LPAREN MINUS MINUS_EQUAL MODULUS MOD_EQUAL NEWLINE NOT NOT_EQUAL NULL OR OR_EQUAL PLUS PLUS_EQUAL PP_DATE PP_DEFINE PP_DTMACRO PP_ERROR PP_FILE PP_IF PP_IFDEF PP_IFNDEF PP_INCLUDE PP_LINE PP_PRAGMA PP_STMACRO PP_TIME PP_TIMESTAMP PP_UNDEF QUESTIONMARK RBRACKET RCURL_BRACE REGISTER RETURN RPAREN SEMICOLON SHIFTL_EQUAL SHIFTR_EQUAL SHIFT_LEFT SHIFT_RIGHT SHORT SIGNED SINGLE_APOS SINGLE_QUOTE SIZEOF STATIC STRING STRUCT SWITCH TILDE TIMES TIMES_EQUAL TYPEDEF UNION UNSIGNED VARNAME VOID VOLTILE VTAB WHILE XOR_EQUAL\n    EXPRESSION : COMENTARIOLEX\n                | VARIABLELEX \n                | OPERATION\n                | DECLARATION\n                | SENTENCIAS\n                | INCLUDE\n                | PREPROCCESOR_DIRECTIVE\n\n    \n    PREPROCCESOR_DIRECTIVE : DEFINE \n                            | INCLUDE\n    \n    DEFINE : PP_DEFINE VARIABLELEX VALUE\n    \n    \n    INCLUDE : PP_INCLUDE HEADER_LIB\n    \n    VALUE : INTEGER\n            | DECIMAL\n    \n    SENTENCIAS : IF\n                | ELSEIF\n                | ELSE\n                | FOR\n                | WHILE\n                | SWITCH\n    \n    DATA_TYPE : INTEGER_TYPE\n            | DECIMAL_TYPE\n            | CHAR\n    \n    INTEGER_TYPE : INT\n                | SHORT\n                | LONG\n    \n    DECIMAL_TYPE : FLOAT\n                | DOUBLE\n    \n    DECLARATION : DATA_TYPE VARNAME EQUAL INTEGER\n    \n    INTEGER_DECLARATION : INTEGER_TYPE VARNAME EQUAL INTEGER\n    \n    DECIMAL_DECLARATION : DECIMAL_TYPE VARNAME EQUAL DECIMAL\n    \n    COMENTARIOLEX : COMMENT\n    \n    VARIABLELEX : VARNAME\n    \n    OPERADOR : PLUS\n              | MINUS\n              | TIMES\n              | MODULUS\n              | DIVIDE\n    \n    OPERATION : VALUE OPERADOR VALUE\n    '
    
_lr_action_items = {'COMMENT':([0,],[9,]),'VARNAME':([0,12,23,24,25,26,27,28,29,30,31,],[10,38,-20,-21,-22,10,-23,-24,-25,-26,-27,]),'IF':([0,],[14,]),'ELSEIF':([0,],[15,]),'ELSE':([0,],[16,]),'FOR':([0,],[17,]),'WHILE':([0,],[18,]),'SWITCH':([0,],[19,]),'PP_INCLUDE':([0,],[20,]),'INTEGER':([0,10,32,33,34,35,36,37,40,42,],[13,-32,13,-33,-34,-35,-36,-37,13,44,]),'DECIMAL':([0,10,32,33,34,35,36,37,40,],[22,-32,22,-33,-34,-35,-36,-37,22,]),'CHAR':([0,],[25,]),'PP_DEFINE':([0,],[26,]),'INT':([0,],[27,]),'SHORT':([0,],[28,]),'LONG':([0,],[29,]),'FLOAT':([0,],[30,]),'DOUBLE':([0,],[31,]),'$end':([1,2,3,4,5,6,7,8,9,10,13,14,15,16,17,18,19,21,22,39,41,43,44,],[0,-1,-2,-3,-4,-5,-6,-7,-31,-32,-12,-14,-15,-16,-17,-18,-19,-8,-13,-11,-38,-10,-28,]),'PLUS':([11,13,22,],[33,-12,-13,]),'MINUS':([11,13,22,],[34,-12,-13,]),'TIMES':([11,13,22,],[35,-12,-13,]),'MODULUS':([11,13,22,],[36,-12,-13,]),'DIVIDE':([11,13,22,],[37,-12,-13,]),'HEADER_LIB':([20,],[39,]),'EQUAL':([38,],[42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'EXPRESSION':([0,],[1,]),'COMENTARIOLEX':([0,],[2,]),'VARIABLELEX':([0,26,],[3,40,]),'OPERATION':([0,],[4,]),'DECLARATION':([0,],[5,]),'SENTENCIAS':([0,],[6,]),'INCLUDE':([0,],[7,]),'PREPROCCESOR_DIRECTIVE':([0,],[8,]),'VALUE':([0,32,40,],[11,41,43,]),'DATA_TYPE':([0,],[12,]),'DEFINE':([0,],[21,]),'INTEGER_TYPE':([0,],[23,]),'DECIMAL_TYPE':([0,],[24,]),'OPERADOR':([11,],[32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> EXPRESSION","S'",1,None,None,None),
  ('EXPRESSION -> COMENTARIOLEX','EXPRESSION',1,'p_EXPRESSION','syntax.py',7),
  ('EXPRESSION -> VARIABLELEX','EXPRESSION',1,'p_EXPRESSION','syntax.py',8),
  ('EXPRESSION -> OPERATION','EXPRESSION',1,'p_EXPRESSION','syntax.py',9),
  ('EXPRESSION -> DECLARATION','EXPRESSION',1,'p_EXPRESSION','syntax.py',10),
  ('EXPRESSION -> SENTENCIAS','EXPRESSION',1,'p_EXPRESSION','syntax.py',11),
  ('EXPRESSION -> INCLUDE','EXPRESSION',1,'p_EXPRESSION','syntax.py',12),
  ('EXPRESSION -> PREPROCCESOR_DIRECTIVE','EXPRESSION',1,'p_EXPRESSION','syntax.py',13),
  ('PREPROCCESOR_DIRECTIVE -> DEFINE','PREPROCCESOR_DIRECTIVE',1,'p_PREPROCCESOR_DIRECTIVE','syntax.py',22),
  ('PREPROCCESOR_DIRECTIVE -> INCLUDE','PREPROCCESOR_DIRECTIVE',1,'p_PREPROCCESOR_DIRECTIVE','syntax.py',23),
  ('DEFINE -> PP_DEFINE VARIABLELEX VALUE','DEFINE',3,'p_DEFINE','syntax.py',29),
  ('INCLUDE -> PP_INCLUDE HEADER_LIB','INCLUDE',2,'p_INCLUDE','syntax.py',36),
  ('VALUE -> INTEGER','VALUE',1,'p_VALUE','syntax.py',43),
  ('VALUE -> DECIMAL','VALUE',1,'p_VALUE','syntax.py',44),
  ('SENTENCIAS -> IF','SENTENCIAS',1,'p_SENTENCIAS','syntax.py',51),
  ('SENTENCIAS -> ELSEIF','SENTENCIAS',1,'p_SENTENCIAS','syntax.py',52),
  ('SENTENCIAS -> ELSE','SENTENCIAS',1,'p_SENTENCIAS','syntax.py',53),
  ('SENTENCIAS -> FOR','SENTENCIAS',1,'p_SENTENCIAS','syntax.py',54),
  ('SENTENCIAS -> WHILE','SENTENCIAS',1,'p_SENTENCIAS','syntax.py',55),
  ('SENTENCIAS -> SWITCH','SENTENCIAS',1,'p_SENTENCIAS','syntax.py',56),
  ('DATA_TYPE -> INTEGER_TYPE','DATA_TYPE',1,'p_DATA_TYPE','syntax.py',63),
  ('DATA_TYPE -> DECIMAL_TYPE','DATA_TYPE',1,'p_DATA_TYPE','syntax.py',64),
  ('DATA_TYPE -> CHAR','DATA_TYPE',1,'p_DATA_TYPE','syntax.py',65),
  ('INTEGER_TYPE -> INT','INTEGER_TYPE',1,'p_INTEGER_TYPE','syntax.py',72),
  ('INTEGER_TYPE -> SHORT','INTEGER_TYPE',1,'p_INTEGER_TYPE','syntax.py',73),
  ('INTEGER_TYPE -> LONG','INTEGER_TYPE',1,'p_INTEGER_TYPE','syntax.py',74),
  ('DECIMAL_TYPE -> FLOAT','DECIMAL_TYPE',1,'p_DECIMAL_TYPE','syntax.py',81),
  ('DECIMAL_TYPE -> DOUBLE','DECIMAL_TYPE',1,'p_DECIMAL_TYPE','syntax.py',82),
  ('DECLARATION -> DATA_TYPE VARNAME EQUAL INTEGER','DECLARATION',4,'p_DECLARATION','syntax.py',89),
  ('INTEGER_DECLARATION -> INTEGER_TYPE VARNAME EQUAL INTEGER','INTEGER_DECLARATION',4,'p_INTEGER_DECLARATION','syntax.py',96),
  ('DECIMAL_DECLARATION -> DECIMAL_TYPE VARNAME EQUAL DECIMAL','DECIMAL_DECLARATION',4,'p_DECIMAL_DECLARATION','syntax.py',103),
  ('COMENTARIOLEX -> COMMENT','COMENTARIOLEX',1,'p_COMENTARIOLEX','syntax.py',112),
  ('VARIABLELEX -> VARNAME','VARIABLELEX',1,'p_VARIABLELEX','syntax.py',119),
  ('OPERADOR -> PLUS','OPERADOR',1,'p_OPERADOR','syntax.py',126),
  ('OPERADOR -> MINUS','OPERADOR',1,'p_OPERADOR','syntax.py',127),
  ('OPERADOR -> TIMES','OPERADOR',1,'p_OPERADOR','syntax.py',128),
  ('OPERADOR -> MODULUS','OPERADOR',1,'p_OPERADOR','syntax.py',129),
  ('OPERADOR -> DIVIDE','OPERADOR',1,'p_OPERADOR','syntax.py',130),
  ('OPERATION -> VALUE OPERADOR VALUE','OPERATION',3,'p_OPERATION','syntax.py',137),
]

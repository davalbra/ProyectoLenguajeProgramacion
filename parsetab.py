
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND ARGUMENTS ASIGNAR AWAIT BOOLEANO BREAK CADENA CASE CATCH CLASS COMA COMENTARIO CONST CONTINUE DCORCHETE DEBUGGER DEFAULT DELETE DIVIDIR DIVISIONIGUAL DLLAVE DO DOSPUNTOS ELSE ENUM EXPORT EXTENDS FALSE FINALLY FLOTANTE FOR FUNCTION ICORCHETE IF IGUALDADESTRICTA ILLAVE IMPLEMENTS IN INSTANCEOF INTERFACE LET LPAREN MAS MASIGUAL MAYORIGUAL MAYOR_QUE MENORIGUAL MENOR_QUE MENOS MENOSIGUAL METODO_ADD_SET METODO_HAS METODO_POP_ARRAY METODO_PUSH_ARRAY METODO_SET METODO_SIZE_SET MODULO MULTIPLICAR NEGACION NEW NOESIGUAL NULL NUMERO OR PACKAGE PORIGUAL PRIVATE PROTECTED PUBLIC PUNTO PUNTOCOMA RETURN RPAREN STATIC SUPER SWITCH THIS THROW TRUE TRY TYPEOF VAR VARIABLE VOID WHILE WITH YIELD STATEMENT : EXPRESSION\n    OPERATOR_MAT : MAS\n                    | MENOS\n                    | MULTIPLICAR\n                    | DIVIDIR\n    EXPRESSION : asignar_variable\n                | ESTRUCTURA_FOR\n                | grupo_datos\n                | FUNCTIONS\n                | declarar_variable\n                | NUMERO\n                | FLOTANTE\n                | EXPRESSION_MAT\n                | EXPRESSION_CONDICION_BOOLEANA\n                | metodos_estructuras\n\n     EXPRESSION_MAT : EXPRESSION_MAT_OPTIONS\n\n        EXPRESSION_MAT_OPTIONS : EXPRESSION_MAT_NUMERO\n                      | EXPRESSION_MAT_FLOTANTE\n\n        EXPRESSION_MAT_NUMERO : EXPRESSION_MAT_NUMERO OPERATOR_MAT EXPRESSION_MAT_NUMERO\n                      | EXPRESSION_MAT_NUMERO OPERATOR_MAT NUMERO\n                      | LPAREN EXPRESSION_MAT_NUMERO RPAREN\n                      | NUMERO OPERATOR_MAT NUMERO\n                      | VARIABLE OPERATOR_MAT VARIABLE\n                      | VARIABLE OPERATOR_MAT NUMERO\n                      | NUMERO OPERATOR_MAT VARIABLE\n\n        EXPRESSION_MAT_FLOTANTE : EXPRESSION_MAT_FLOTANTE OPERATOR_MAT EXPRESSION_MAT_FLOTANTE\n                      | EXPRESSION_MAT_FLOTANTE OPERATOR_MAT FLOTANTE\n                      | FLOTANTE OPERATOR_MAT FLOTANTE\n                      | LPAREN EXPRESSION_MAT_FLOTANTE RPAREN\n                      | VARIABLE OPERATOR_MAT VARIABLE\n                      | VARIABLE OPERATOR_MAT FLOTANTE\n                      | FLOTANTE OPERATOR_MAT VARIABLE\n     EXPRESSION_CONDICION_BOOLEANA : COMPARACION OPERATOR_COMP_MAT COMPARACION\n    COMPARACION : VARIABLE\n                    | NUMERO\n                    | BOOLEANO\n    OPERATOR_COMP_MAT : IGUALDADESTRICTA\n                    | MAYORIGUAL\n                    | MENORIGUAL\n                    | MENOR_QUE\n                    | MAYOR_QUE\n                    | AND\n                    | OR\n                    | NOESIGUAL\n    grupo_datos : tipos_datos\n                    | tipos_datos COMA grupo_datosasignar_variable : declarar_variable ASIGNAR tipos_datos PUNTOCOMA\n                        | VARIABLE ASIGNAR VARIABLE PUNTOCOMA\n                        | VARIABLE ASIGNAR tipos_datos PUNTOCOMA\n                        | declarar_variable ASIGNAR iniciar_estructuras\n                        | declarar_variable ASIGNAR iniciar_array\n                        declarar_variable : tipo_variable VARIABLE PUNTOCOMA\n                        | tipo_variable VARIABLE\n                        metodos_estructuras : VARIABLE  metodos_array\n                            | VARIABLE metodos_set\n                            | VARIABLE metodos_mapmetodos_array : METODO_POP_ARRAY LPAREN RPAREN PUNTOCOMA\n                    | METODO_PUSH_ARRAY LPAREN MASPARAMETROS RPAREN PUNTOCOMAmetodos_set : METODO_ADD_SET LPAREN MASPARAMETROS RPAREN PUNTOCOMA\n                    | METODO_SIZE_SET PUNTOCOMAmetodos_map : METODO_SET LPAREN tipos_datos COMA tipos_datos RPAREN PUNTOCOMA\n                    | METODO_HAS LPAREN tipos_datos RPAREN PUNTOCOMAiniciar_estructuras : NEW VARIABLE LPAREN RPAREN PUNTOCOMA tipos_datos : booleano_tipo\n                    | NUMERO\n                    | CADENA\n                    | FLOTANTE\n                    | NULLtipo_variable : VAR\n                    | LET\n                    | CONSTiniciar_array : ICORCHETE DCORCHETE\n                    | ICORCHETE repeticion_bool DCORCHETE\n                    | ICORCHETE repeticion_flotante DCORCHETE\n                    | ICORCHETE repeticion_null DCORCHETE\n                    | ICORCHETE repeticion_cadena DCORCHETE\n                    | ICORCHETE repeticion_numero DCORCHETErepeticion_flotante : FLOTANTE\n                            | repeticion_flotante COMA FLOTANTErepeticion_null : NULL\n                        | repeticion_null COMA NULLrepeticion_cadena : CADENA\n                            | repeticion_cadena COMA CADENArepeticion_numero : NUMERO\n                            | repeticion_numero COMA NUMEROrepeticion_bool : booleano_tipo\n                        | repeticion_bool COMA booleano_tipobooleano_tipo : TRUE\n                    | FALSEcadenas_caracteres : CADENA FUNCTIONS : FUNCTION VARIABLE LPAREN MASPARAMETROS RPAREN ILLAVE DLLAVE\n                  | FUNCTION VARIABLE LPAREN MASPARAMETROS RPAREN ILLAVE RETURN MASPARAMETROS DLLAVE\n    MASPARAMETROS : PARAMETROS VAR\n                    | PARAMETROS COMA MASPARAMETROS\n    PARAMETROS :  tipos_datos\n                    | VARIABLE\n    ESTRUCTURA_FOR : FOR LPAREN asignar_variable EXPRESSION_CONDICION_BOOLEANA PUNTOCOMA VARIABLE MAS MAS RPAREN ILLAVE DLLAVE\n    '
    
_lr_action_items = {'NUMERO':([0,16,32,33,34,35,36,37,39,40,44,59,60,61,62,63,64,65,66,67,68,71,72,76,88,89,91,92,93,98,105,111,113,124,125,136,139,141,143,145,147,148,152,154,173,177,],[8,54,73,77,-2,-3,-4,-5,73,73,85,102,-37,-38,-39,-40,-41,-42,-43,-44,104,-50,-51,123,73,73,73,73,102,73,54,-47,-72,-48,-49,85,-73,-74,-75,-76,-77,165,73,73,-63,73,]),'FLOTANTE':([0,16,32,34,35,36,37,38,39,40,44,69,76,88,89,91,92,98,109,137,142,152,154,177,],[9,56,74,-2,-3,-4,-5,79,74,74,86,108,120,74,74,74,74,74,56,86,162,74,74,74,]),'VARIABLE':([0,16,17,18,24,25,26,33,34,35,36,37,38,40,44,51,59,60,61,62,63,64,65,66,67,68,69,71,72,75,88,89,93,98,105,109,111,113,124,125,136,137,139,141,143,145,147,152,156,173,177,],[14,55,57,58,-69,-70,-71,78,-2,-3,-4,-5,80,82,84,94,101,-37,-38,-39,-40,-41,-42,-43,-44,106,110,-50,-51,112,130,130,101,130,106,110,-47,-72,-48,-49,158,159,-73,-74,-75,-76,-77,130,171,-63,130,]),'FOR':([0,],[15,]),'FUNCTION':([0,],[17,]),'CADENA':([0,32,39,40,76,88,89,91,92,98,146,152,154,177,],[22,22,22,22,122,22,22,22,22,22,164,22,22,22,]),'NULL':([0,32,39,40,76,88,89,91,92,98,144,152,154,177,],[23,23,23,23,121,23,23,23,23,23,163,23,23,23,]),'VAR':([0,21,22,23,30,31,51,73,74,128,129,130,],[24,-64,-66,-68,-88,-89,24,-65,-67,151,-95,-96,]),'LET':([0,51,],[25,25,]),'CONST':([0,51,],[26,26,]),'BOOLEANO':([0,59,60,61,62,63,64,65,66,67,71,72,93,111,113,124,125,139,141,143,145,147,173,],[29,29,-37,-38,-39,-40,-41,-42,-43,-44,-50,-51,29,-47,-72,-48,-49,-73,-74,-75,-76,-77,-63,]),'TRUE':([0,32,39,40,76,88,89,91,92,98,140,152,154,177,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'FALSE':([0,32,39,40,76,88,89,91,92,98,140,152,154,177,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'LPAREN':([0,15,16,34,35,36,37,45,46,47,49,50,57,68,69,105,109,112,],[16,51,16,-2,-3,-4,-5,87,88,89,91,92,98,105,109,105,109,138,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,19,21,22,23,27,28,29,30,31,41,42,43,58,71,72,73,74,77,78,79,80,81,84,85,86,90,96,97,99,100,101,102,103,104,107,108,111,113,124,125,139,141,143,145,147,149,158,159,166,168,170,173,176,178,182,184,],[0,-1,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-45,-16,-64,-66,-68,-17,-18,-36,-88,-89,-54,-55,-56,-53,-50,-51,-65,-67,-22,-25,-28,-32,-46,-23,-24,-31,-60,-21,-29,-52,-33,-34,-35,-19,-20,-26,-27,-47,-72,-48,-49,-73,-74,-75,-76,-77,-57,-23,-30,-58,-59,-62,-63,-91,-61,-92,-97,]),'ASIGNAR':([7,14,58,94,95,99,],[32,40,-53,40,32,-52,]),'COMA':([8,9,13,21,22,23,30,31,73,74,114,115,116,117,118,119,120,121,122,123,128,129,130,132,161,162,163,164,165,],[-65,-67,39,-64,-66,-68,-88,-89,-65,-67,140,142,144,146,148,-86,-78,-80,-82,-84,152,-95,-96,154,-87,-79,-81,-83,-85,]),'IGUALDADESTRICTA':([8,14,20,29,101,102,],[-35,-34,60,-36,-34,-35,]),'MAYORIGUAL':([8,14,20,29,101,102,],[-35,-34,61,-36,-34,-35,]),'MENORIGUAL':([8,14,20,29,101,102,],[-35,-34,62,-36,-34,-35,]),'MENOR_QUE':([8,14,20,29,101,102,],[-35,-34,63,-36,-34,-35,]),'MAYOR_QUE':([8,14,20,29,101,102,],[-35,-34,64,-36,-34,-35,]),'AND':([8,14,20,29,101,102,],[-35,-34,65,-36,-34,-35,]),'OR':([8,14,20,29,101,102,],[-35,-34,66,-36,-34,-35,]),'NOESIGUAL':([8,14,20,29,101,102,],[-35,-34,67,-36,-34,-35,]),'MAS':([8,9,14,27,28,52,53,54,55,56,77,78,79,80,84,85,86,96,97,103,104,106,107,108,110,158,159,171,175,],[34,34,34,34,34,34,34,34,34,34,-22,-25,-28,-32,-23,-24,-31,-21,-29,34,34,34,34,34,34,-23,-30,175,179,]),'MENOS':([8,9,14,27,28,52,53,54,55,56,77,78,79,80,84,85,86,96,97,103,104,106,107,108,110,158,159,],[35,35,35,35,35,35,35,35,35,35,-22,-25,-28,-32,-23,-24,-31,-21,-29,35,35,35,35,35,35,-23,-30,]),'MULTIPLICAR':([8,9,14,27,28,52,53,54,55,56,77,78,79,80,84,85,86,96,97,103,104,106,107,108,110,158,159,],[36,36,36,36,36,36,36,36,36,36,-22,-25,-28,-32,-23,-24,-31,-21,-29,36,36,36,36,36,36,-23,-30,]),'DIVIDIR':([8,9,14,27,28,52,53,54,55,56,77,78,79,80,84,85,86,96,97,103,104,106,107,108,110,158,159,],[37,37,37,37,37,37,37,37,37,37,-22,-25,-28,-32,-23,-24,-31,-21,-29,37,37,37,37,37,37,-23,-30,]),'METODO_POP_ARRAY':([14,],[45,]),'METODO_PUSH_ARRAY':([14,],[46,]),'METODO_ADD_SET':([14,],[47,]),'METODO_SIZE_SET':([14,],[48,]),'METODO_SET':([14,],[49,]),'METODO_HAS':([14,],[50,]),'PUNTOCOMA':([21,22,23,29,30,31,48,58,70,73,74,82,83,100,101,102,126,134,150,153,155,160,174,],[-64,-66,-68,-36,-88,-89,90,99,111,-65,-67,124,125,-33,-34,-35,149,156,166,168,170,173,178,]),'RPAREN':([21,22,23,30,31,52,53,73,74,77,78,79,80,84,85,86,87,96,97,103,104,107,108,127,131,133,135,138,151,158,159,167,169,179,],[-64,-66,-68,-88,-89,96,97,-65,-67,-22,-25,-28,-32,-23,-24,-31,126,-21,-29,-19,-20,-26,-27,150,153,155,157,160,-93,-23,-30,-94,174,181,]),'DCORCHETE':([30,31,76,114,115,116,117,118,119,120,121,122,123,161,162,163,164,165,],[-88,-89,113,139,141,143,145,147,-86,-78,-80,-82,-84,-87,-79,-81,-83,-85,]),'NEW':([32,],[75,]),'ICORCHETE':([32,],[76,]),'DLLAVE':([151,167,172,180,183,],[-93,-94,176,182,184,]),'ILLAVE':([157,181,],[172,183,]),'RETURN':([172,],[177,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'STATEMENT':([0,],[1,]),'EXPRESSION':([0,],[2,]),'asignar_variable':([0,51,],[3,93,]),'ESTRUCTURA_FOR':([0,],[4,]),'grupo_datos':([0,39,],[5,81,]),'FUNCTIONS':([0,],[6,]),'declarar_variable':([0,51,],[7,95,]),'EXPRESSION_MAT':([0,],[10,]),'EXPRESSION_CONDICION_BOOLEANA':([0,93,],[11,134,]),'metodos_estructuras':([0,],[12,]),'tipos_datos':([0,32,39,40,88,89,91,92,98,152,154,177,],[13,70,13,83,129,129,132,133,129,129,169,129,]),'tipo_variable':([0,51,],[18,18,]),'EXPRESSION_MAT_OPTIONS':([0,],[19,]),'COMPARACION':([0,59,93,],[20,100,20,]),'booleano_tipo':([0,32,39,40,76,88,89,91,92,98,140,152,154,177,],[21,21,21,21,119,21,21,21,21,21,161,21,21,21,]),'EXPRESSION_MAT_NUMERO':([0,16,68,105,],[27,52,103,52,]),'EXPRESSION_MAT_FLOTANTE':([0,16,69,109,],[28,53,107,53,]),'OPERATOR_MAT':([8,9,14,27,28,52,53,54,55,56,103,104,106,107,108,110,],[33,38,44,68,69,68,69,33,44,38,68,33,136,69,38,137,]),'metodos_array':([14,],[41,]),'metodos_set':([14,],[42,]),'metodos_map':([14,],[43,]),'OPERATOR_COMP_MAT':([20,],[59,]),'iniciar_estructuras':([32,],[71,]),'iniciar_array':([32,],[72,]),'repeticion_bool':([76,],[114,]),'repeticion_flotante':([76,],[115,]),'repeticion_null':([76,],[116,]),'repeticion_cadena':([76,],[117,]),'repeticion_numero':([76,],[118,]),'MASPARAMETROS':([88,89,98,152,177,],[127,131,135,167,180,]),'PARAMETROS':([88,89,98,152,177,],[128,128,128,128,128,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> STATEMENT","S'",1,None,None,None),
  ('STATEMENT -> EXPRESSION','STATEMENT',1,'p_STATEMENT','sictactico_javascript.py',8),
  ('OPERATOR_MAT -> MAS','OPERATOR_MAT',1,'p_OPERATOR_MAT','sictactico_javascript.py',13),
  ('OPERATOR_MAT -> MENOS','OPERATOR_MAT',1,'p_OPERATOR_MAT','sictactico_javascript.py',14),
  ('OPERATOR_MAT -> MULTIPLICAR','OPERATOR_MAT',1,'p_OPERATOR_MAT','sictactico_javascript.py',15),
  ('OPERATOR_MAT -> DIVIDIR','OPERATOR_MAT',1,'p_OPERATOR_MAT','sictactico_javascript.py',16),
  ('EXPRESSION -> asignar_variable','EXPRESSION',1,'p_EXPRESSION','sictactico_javascript.py',21),
  ('EXPRESSION -> ESTRUCTURA_FOR','EXPRESSION',1,'p_EXPRESSION','sictactico_javascript.py',22),
  ('EXPRESSION -> grupo_datos','EXPRESSION',1,'p_EXPRESSION','sictactico_javascript.py',23),
  ('EXPRESSION -> FUNCTIONS','EXPRESSION',1,'p_EXPRESSION','sictactico_javascript.py',24),
  ('EXPRESSION -> declarar_variable','EXPRESSION',1,'p_EXPRESSION','sictactico_javascript.py',25),
  ('EXPRESSION -> NUMERO','EXPRESSION',1,'p_EXPRESSION','sictactico_javascript.py',26),
  ('EXPRESSION -> FLOTANTE','EXPRESSION',1,'p_EXPRESSION','sictactico_javascript.py',27),
  ('EXPRESSION -> EXPRESSION_MAT','EXPRESSION',1,'p_EXPRESSION','sictactico_javascript.py',28),
  ('EXPRESSION -> EXPRESSION_CONDICION_BOOLEANA','EXPRESSION',1,'p_EXPRESSION','sictactico_javascript.py',29),
  ('EXPRESSION -> metodos_estructuras','EXPRESSION',1,'p_EXPRESSION','sictactico_javascript.py',30),
  ('EXPRESSION_MAT -> EXPRESSION_MAT_OPTIONS','EXPRESSION_MAT',1,'p_EXPRESSION_MAT','sictactico_javascript.py',36),
  ('EXPRESSION_MAT_OPTIONS -> EXPRESSION_MAT_NUMERO','EXPRESSION_MAT_OPTIONS',1,'p_EXPRESSION_MAT','sictactico_javascript.py',38),
  ('EXPRESSION_MAT_OPTIONS -> EXPRESSION_MAT_FLOTANTE','EXPRESSION_MAT_OPTIONS',1,'p_EXPRESSION_MAT','sictactico_javascript.py',39),
  ('EXPRESSION_MAT_NUMERO -> EXPRESSION_MAT_NUMERO OPERATOR_MAT EXPRESSION_MAT_NUMERO','EXPRESSION_MAT_NUMERO',3,'p_EXPRESSION_MAT','sictactico_javascript.py',41),
  ('EXPRESSION_MAT_NUMERO -> EXPRESSION_MAT_NUMERO OPERATOR_MAT NUMERO','EXPRESSION_MAT_NUMERO',3,'p_EXPRESSION_MAT','sictactico_javascript.py',42),
  ('EXPRESSION_MAT_NUMERO -> LPAREN EXPRESSION_MAT_NUMERO RPAREN','EXPRESSION_MAT_NUMERO',3,'p_EXPRESSION_MAT','sictactico_javascript.py',43),
  ('EXPRESSION_MAT_NUMERO -> NUMERO OPERATOR_MAT NUMERO','EXPRESSION_MAT_NUMERO',3,'p_EXPRESSION_MAT','sictactico_javascript.py',44),
  ('EXPRESSION_MAT_NUMERO -> VARIABLE OPERATOR_MAT VARIABLE','EXPRESSION_MAT_NUMERO',3,'p_EXPRESSION_MAT','sictactico_javascript.py',45),
  ('EXPRESSION_MAT_NUMERO -> VARIABLE OPERATOR_MAT NUMERO','EXPRESSION_MAT_NUMERO',3,'p_EXPRESSION_MAT','sictactico_javascript.py',46),
  ('EXPRESSION_MAT_NUMERO -> NUMERO OPERATOR_MAT VARIABLE','EXPRESSION_MAT_NUMERO',3,'p_EXPRESSION_MAT','sictactico_javascript.py',47),
  ('EXPRESSION_MAT_FLOTANTE -> EXPRESSION_MAT_FLOTANTE OPERATOR_MAT EXPRESSION_MAT_FLOTANTE','EXPRESSION_MAT_FLOTANTE',3,'p_EXPRESSION_MAT','sictactico_javascript.py',49),
  ('EXPRESSION_MAT_FLOTANTE -> EXPRESSION_MAT_FLOTANTE OPERATOR_MAT FLOTANTE','EXPRESSION_MAT_FLOTANTE',3,'p_EXPRESSION_MAT','sictactico_javascript.py',50),
  ('EXPRESSION_MAT_FLOTANTE -> FLOTANTE OPERATOR_MAT FLOTANTE','EXPRESSION_MAT_FLOTANTE',3,'p_EXPRESSION_MAT','sictactico_javascript.py',51),
  ('EXPRESSION_MAT_FLOTANTE -> LPAREN EXPRESSION_MAT_FLOTANTE RPAREN','EXPRESSION_MAT_FLOTANTE',3,'p_EXPRESSION_MAT','sictactico_javascript.py',52),
  ('EXPRESSION_MAT_FLOTANTE -> VARIABLE OPERATOR_MAT VARIABLE','EXPRESSION_MAT_FLOTANTE',3,'p_EXPRESSION_MAT','sictactico_javascript.py',53),
  ('EXPRESSION_MAT_FLOTANTE -> VARIABLE OPERATOR_MAT FLOTANTE','EXPRESSION_MAT_FLOTANTE',3,'p_EXPRESSION_MAT','sictactico_javascript.py',54),
  ('EXPRESSION_MAT_FLOTANTE -> FLOTANTE OPERATOR_MAT VARIABLE','EXPRESSION_MAT_FLOTANTE',3,'p_EXPRESSION_MAT','sictactico_javascript.py',55),
  ('EXPRESSION_CONDICION_BOOLEANA -> COMPARACION OPERATOR_COMP_MAT COMPARACION','EXPRESSION_CONDICION_BOOLEANA',3,'p_EXPRESSION_CONDICION_BOOLEANA','sictactico_javascript.py',61),
  ('COMPARACION -> VARIABLE','COMPARACION',1,'p_COMPARACION','sictactico_javascript.py',65),
  ('COMPARACION -> NUMERO','COMPARACION',1,'p_COMPARACION','sictactico_javascript.py',66),
  ('COMPARACION -> BOOLEANO','COMPARACION',1,'p_COMPARACION','sictactico_javascript.py',67),
  ('OPERATOR_COMP_MAT -> IGUALDADESTRICTA','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sictactico_javascript.py',74),
  ('OPERATOR_COMP_MAT -> MAYORIGUAL','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sictactico_javascript.py',75),
  ('OPERATOR_COMP_MAT -> MENORIGUAL','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sictactico_javascript.py',76),
  ('OPERATOR_COMP_MAT -> MENOR_QUE','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sictactico_javascript.py',77),
  ('OPERATOR_COMP_MAT -> MAYOR_QUE','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sictactico_javascript.py',78),
  ('OPERATOR_COMP_MAT -> AND','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sictactico_javascript.py',79),
  ('OPERATOR_COMP_MAT -> OR','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sictactico_javascript.py',80),
  ('OPERATOR_COMP_MAT -> NOESIGUAL','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sictactico_javascript.py',81),
  ('grupo_datos -> tipos_datos','grupo_datos',1,'p_grupo_datos','sictactico_javascript.py',87),
  ('grupo_datos -> tipos_datos COMA grupo_datos','grupo_datos',3,'p_grupo_datos','sictactico_javascript.py',88),
  ('asignar_variable -> declarar_variable ASIGNAR tipos_datos PUNTOCOMA','asignar_variable',4,'p_asignar_variable','sictactico_javascript.py',98),
  ('asignar_variable -> VARIABLE ASIGNAR VARIABLE PUNTOCOMA','asignar_variable',4,'p_asignar_variable','sictactico_javascript.py',99),
  ('asignar_variable -> VARIABLE ASIGNAR tipos_datos PUNTOCOMA','asignar_variable',4,'p_asignar_variable','sictactico_javascript.py',100),
  ('asignar_variable -> declarar_variable ASIGNAR iniciar_estructuras','asignar_variable',3,'p_asignar_variable','sictactico_javascript.py',101),
  ('asignar_variable -> declarar_variable ASIGNAR iniciar_array','asignar_variable',3,'p_asignar_variable','sictactico_javascript.py',102),
  ('declarar_variable -> tipo_variable VARIABLE PUNTOCOMA','declarar_variable',3,'p_declarar_variable','sictactico_javascript.py',107),
  ('declarar_variable -> tipo_variable VARIABLE','declarar_variable',2,'p_declarar_variable','sictactico_javascript.py',108),
  ('metodos_estructuras -> VARIABLE metodos_array','metodos_estructuras',2,'p_metodos_estructuras','sictactico_javascript.py',114),
  ('metodos_estructuras -> VARIABLE metodos_set','metodos_estructuras',2,'p_metodos_estructuras','sictactico_javascript.py',115),
  ('metodos_estructuras -> VARIABLE metodos_map','metodos_estructuras',2,'p_metodos_estructuras','sictactico_javascript.py',116),
  ('metodos_array -> METODO_POP_ARRAY LPAREN RPAREN PUNTOCOMA','metodos_array',4,'p_metodos_array','sictactico_javascript.py',119),
  ('metodos_array -> METODO_PUSH_ARRAY LPAREN MASPARAMETROS RPAREN PUNTOCOMA','metodos_array',5,'p_metodos_array','sictactico_javascript.py',120),
  ('metodos_set -> METODO_ADD_SET LPAREN MASPARAMETROS RPAREN PUNTOCOMA','metodos_set',5,'p_metodos_set','sictactico_javascript.py',123),
  ('metodos_set -> METODO_SIZE_SET PUNTOCOMA','metodos_set',2,'p_metodos_set','sictactico_javascript.py',124),
  ('metodos_map -> METODO_SET LPAREN tipos_datos COMA tipos_datos RPAREN PUNTOCOMA','metodos_map',7,'p_metodos_map','sictactico_javascript.py',127),
  ('metodos_map -> METODO_HAS LPAREN tipos_datos RPAREN PUNTOCOMA','metodos_map',5,'p_metodos_map','sictactico_javascript.py',128),
  ('iniciar_estructuras -> NEW VARIABLE LPAREN RPAREN PUNTOCOMA','iniciar_estructuras',5,'p_iniciar_estructuras','sictactico_javascript.py',132),
  ('tipos_datos -> booleano_tipo','tipos_datos',1,'p_tipos_datos','sictactico_javascript.py',137),
  ('tipos_datos -> NUMERO','tipos_datos',1,'p_tipos_datos','sictactico_javascript.py',138),
  ('tipos_datos -> CADENA','tipos_datos',1,'p_tipos_datos','sictactico_javascript.py',139),
  ('tipos_datos -> FLOTANTE','tipos_datos',1,'p_tipos_datos','sictactico_javascript.py',140),
  ('tipos_datos -> NULL','tipos_datos',1,'p_tipos_datos','sictactico_javascript.py',141),
  ('tipo_variable -> VAR','tipo_variable',1,'p_tipo_variable','sictactico_javascript.py',148),
  ('tipo_variable -> LET','tipo_variable',1,'p_tipo_variable','sictactico_javascript.py',149),
  ('tipo_variable -> CONST','tipo_variable',1,'p_tipo_variable','sictactico_javascript.py',150),
  ('iniciar_array -> ICORCHETE DCORCHETE','iniciar_array',2,'p_iniciar_array','sictactico_javascript.py',154),
  ('iniciar_array -> ICORCHETE repeticion_bool DCORCHETE','iniciar_array',3,'p_iniciar_array','sictactico_javascript.py',155),
  ('iniciar_array -> ICORCHETE repeticion_flotante DCORCHETE','iniciar_array',3,'p_iniciar_array','sictactico_javascript.py',156),
  ('iniciar_array -> ICORCHETE repeticion_null DCORCHETE','iniciar_array',3,'p_iniciar_array','sictactico_javascript.py',157),
  ('iniciar_array -> ICORCHETE repeticion_cadena DCORCHETE','iniciar_array',3,'p_iniciar_array','sictactico_javascript.py',158),
  ('iniciar_array -> ICORCHETE repeticion_numero DCORCHETE','iniciar_array',3,'p_iniciar_array','sictactico_javascript.py',159),
  ('repeticion_flotante -> FLOTANTE','repeticion_flotante',1,'p_repeticion_flotante','sictactico_javascript.py',162),
  ('repeticion_flotante -> repeticion_flotante COMA FLOTANTE','repeticion_flotante',3,'p_repeticion_flotante','sictactico_javascript.py',163),
  ('repeticion_null -> NULL','repeticion_null',1,'p_repeticion_null','sictactico_javascript.py',166),
  ('repeticion_null -> repeticion_null COMA NULL','repeticion_null',3,'p_repeticion_null','sictactico_javascript.py',167),
  ('repeticion_cadena -> CADENA','repeticion_cadena',1,'p_repeticion_cadena','sictactico_javascript.py',170),
  ('repeticion_cadena -> repeticion_cadena COMA CADENA','repeticion_cadena',3,'p_repeticion_cadena','sictactico_javascript.py',171),
  ('repeticion_numero -> NUMERO','repeticion_numero',1,'p_repeticion_numero','sictactico_javascript.py',174),
  ('repeticion_numero -> repeticion_numero COMA NUMERO','repeticion_numero',3,'p_repeticion_numero','sictactico_javascript.py',175),
  ('repeticion_bool -> booleano_tipo','repeticion_bool',1,'p_repeticion_bool','sictactico_javascript.py',178),
  ('repeticion_bool -> repeticion_bool COMA booleano_tipo','repeticion_bool',3,'p_repeticion_bool','sictactico_javascript.py',179),
  ('booleano_tipo -> TRUE','booleano_tipo',1,'p_booleano_tipo','sictactico_javascript.py',183),
  ('booleano_tipo -> FALSE','booleano_tipo',1,'p_booleano_tipo','sictactico_javascript.py',184),
  ('cadenas_caracteres -> CADENA','cadenas_caracteres',1,'p_cadenas_caracteres','sictactico_javascript.py',189),
  ('FUNCTIONS -> FUNCTION VARIABLE LPAREN MASPARAMETROS RPAREN ILLAVE DLLAVE','FUNCTIONS',7,'p_FUNCTIONS','sictactico_javascript.py',195),
  ('FUNCTIONS -> FUNCTION VARIABLE LPAREN MASPARAMETROS RPAREN ILLAVE RETURN MASPARAMETROS DLLAVE','FUNCTIONS',9,'p_FUNCTIONS','sictactico_javascript.py',196),
  ('MASPARAMETROS -> PARAMETROS VAR','MASPARAMETROS',2,'p_MASPARAMETROS','sictactico_javascript.py',200),
  ('MASPARAMETROS -> PARAMETROS COMA MASPARAMETROS','MASPARAMETROS',3,'p_MASPARAMETROS','sictactico_javascript.py',201),
  ('PARAMETROS -> tipos_datos','PARAMETROS',1,'p_PARAMETROS','sictactico_javascript.py',206),
  ('PARAMETROS -> VARIABLE','PARAMETROS',1,'p_PARAMETROS','sictactico_javascript.py',207),
  ('ESTRUCTURA_FOR -> FOR LPAREN asignar_variable EXPRESSION_CONDICION_BOOLEANA PUNTOCOMA VARIABLE MAS MAS RPAREN ILLAVE DLLAVE','ESTRUCTURA_FOR',11,'p_ESTRUCTURA_FOR','sictactico_javascript.py',221),
]

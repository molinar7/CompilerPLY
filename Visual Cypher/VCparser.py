import VCscanner as lexer
import ply.yacc as yacc
import sys
import VCsemantics
from VCquadruples import * # con esto ya no es necesario poner el nombre de la clase
import VCmemory


tokens = lexer.tokens
tmp_type = ''

param_counter = 0
functionIndex_onCall = 0

def p_program(p):
	'''
	program		:	PROGRAM  ID  LCURLY_BRACKET  vars   add_NumVars_Main_Global function 	main_function	 RCURLY_BRACKET	

	'''
	p[0] = "Syntax Accepted!"


def p_vars(p):
	'''
	vars	:	type	save_type	ID		pushTo_varsTable	vars_prime		SEMICOLON		vars
			|	epsilon
	'''
def p_vars_prime(p):
	'''
	vars_prime		:	COMA	ID	pushTo_varsTable	vars_prime
					|	epsilon
	'''





def p_pushTo_varsTable(p):
	'pushTo_varsTable	:	epsilon'
	VCsemantics.pushTo_varsTable(p[-1], tmp_type, str(p.lexer.lineno))
	

def p_save_type(p):
	'save_type	:	epsilon'
	global tmp_type
	tmp_type = p[-1]
	
def p_function(p):
	'''
	function	:	FUNCTION	type	ID		pushTo_FunctionDir		OP_LPAREN		function_parameters OP_RPAREN	add_Function_FirstQuadruple		pushTo_functionSignature			function_bloque		add_NumVars		function
				|	FUNCTION	VOID	ID		pushTo_FunctionDir		OP_LPAREN		function_parameters OP_RPAREN	add_Function_FirstQuadruple		pushTo_functionSignature			function_bloque		add_NumVars		function
				|	epsilon
	'''
def p_pushTo_FunctionDir(p):
	'''
	pushTo_FunctionDir	:	epsilon
	'''
	VCsemantics.pushTo_FunctionDir(p[-1],p[-2], str(p.lexer.lineno))

def p_pushTo_functionSignature(p): #Se encarga de generar la lista de la estructura de los parametros
	'pushTo_functionSignature	:	epsilon'
	index = len(VCsemantics.functionDir)

	# este if sirve par que ponga unicamente indices en funciones con parametros
	if VCsemantics.varsTable[-1][0] == index:
		VCsemantics.functionSignature.append([index])
	numberOfParameters = 0

	for elements in VCsemantics.varsTable:
		if elements[0] == index:
			VCsemantics.functionSignature[-1].append([elements[2], elements[3]]) # cambiar el 3 a 1 si quieres saber el nombre de la var
			numberOfParameters += 1

	VCsemantics.functionDir[-1].append(numberOfParameters)# le ponemos al directorio de funciones la cantidad de parametros
		
def p_add_NumVars(p):
	' add_NumVars	:	epsilon'
	index = len(VCsemantics.functionDir)

	numVars = 0

	for elements in VCsemantics.varsTable:
		if elements[0] == index:
			numVars +=1

	numVars = numVars - VCsemantics.functionDir[-1][4] # Le restamos la cantidad de parametros ya que los parametros ya los tenemos contados
	VCsemantics.functionDir[-1].append(numVars)# metemos la cantidad de variables definidad a functiondir

	quadruples.append(['ENDPROC', '', '', ''])

def p_add_Function_FirstQuadruple(p):
	'add_Function_FirstQuadruple	:	epsilon'
	quadrupleCount = len(quadruples) 
	VCsemantics.functionDir[-1].append(quadrupleCount) # El cuadruplo que dice cuando se acaba una funcion

def p_main_function(p):
	'''
	main_function	:	MAIN	pushTo_FunctionDir OP_LPAREN	OP_RPAREN 	fill_firstQuadruple		function_bloque	add_NumVars_Main_Global push_end_quadruple
	'''

def p_fill_firstQuadruple(p):
	' fill_firstQuadruple	:	epsilon'
	quadrupleCount = len(quadruples)
	quadruples[0][3] = quadrupleCount # pone el counter en el primer quadruplo del main
	VCsemantics.functionDir[-1].append(len(quadruples))# pone el cuadruplo donde empieza el main en la function dir
	index = len(VCsemantics.functionDir)

def p_add_NumVars_Main_Global(p):
	' add_NumVars_Main_Global	:	epsilon'
	index = len(VCsemantics.functionDir)

	numVars = 0

	for elements in VCsemantics.varsTable:
		if elements[0] == index:
			numVars +=1

	# este if llena el cuadruplo donde empieza la funcion global porque el de main ya lo llenamos con 'p_fill_firstQuadruple'
	if VCsemantics.functionDir[-1][1] == 'global':# Empieza global en el cuadruplo 0
		VCsemantics.functionDir[-1].append(0)# pone el cuadruplo donde empieza  global en function dir

	
	VCsemantics.functionDir[-1].append(0) # le ponemos siempre 0 porque main y global tiene 0 parametros
	numVars = numVars - VCsemantics.functionDir[-1][4] # Le restamos la cantidad de parametros ya que los parametros ya los tenemos contados
	VCsemantics.functionDir[-1].append(numVars)# metemos la cantidad de variables definidad a functiondir


def p_push_end_quadruple(p):
	'push_end_quadruple	: epsilon'
	quadruples.append(['END', '', '',''])# cuadruplo que dice cuando acaba el programa
def p_type(p):
	'''
	type	:	INT
			|	FLOAT
			|	STRING
			|	BOOLEAN
			
	'''
	p[0] = p[1]
def p_function_parameters(p):
	'''
	function_parameters	:	type	save_type	ID		pushTo_varsTable	function_parameters_prime
						|	epsilon
	'''
def p_function_parameters_prime(p):
	'''
	function_parameters_prime	:	COMA	type	save_type	ID	pushTo_varsTable	function_parameters_prime
								|	epsilon
	'''
def p_function_bloque(p):
	'''
	function_bloque	:	LCURLY_BRACKET	function_bloque_primo	RCURLY_BRACKET	
	
	'''
def p_function_bloque_primo(p):
	'''
	function_bloque_primo	:	function_bloque_primo	function_statement 
							|	epsilon
			
	'''

#Statement de las funciones	
def	p_function_statement(p):# Para prevenir la creacion de vars  en los bloques de los ciclos
	'''
	function_statement	:	assigment
						|	if
						|	printer
						|	increment
						|	for
						|	return
						|	function_call
						|	fun_esp
						|	vars
						|	while_loop
				
	'''	
def p_bloque(p):
	'''
	bloque	:	LCURLY_BRACKET	bloque_primo	RCURLY_BRACKET	
	
	'''

def p_bloque_primo(p):
	'''
	bloque_primo	:	bloque_primo	statement 
					|	epsilon
			
	'''	
def	p_statement(p):
	'''
	statement	:	assigment
				|	if
				|	printer
				|	increment
				|	for
				|	return
				|	function_call
				|	fun_esp
				|	while_loop
				
	'''

def p_assigment(p):
	'''
	assigment	:	ID		push_varID_to_Stack		OP_EQUALS	push_symbol				mega_expression			equals_quadruple	SEMICOLON
				|	ID		OP_LSQUARE_PAREN		VAR_INT		OP_RSQUARE_PAREN		OP_EQUALS				mega_expression		SEMICOLON
	'''

def p_equals_quadruple(p):
	'equals_quadruple	:	epsilon'
	right_op = stackOP.pop()
	right_type = stackType.pop()

	left_op = stackOP.pop()
	left_type = stackType.pop()

	operator = stackSymbol.pop()


	if left_type == right_type:
		quadruples.append([operator,right_op,'',left_op])
		
	else:
		print ("Type mismatch error at line  " + str(p.lexer.lineno))
		quit()

def p_if (p):
	'''
	if	:	IF	OP_LPAREN	mega_expression	OP_RPAREN 	if_gotoF_quadruple	bloque	fill_if_gotoF1
		|	IF	OP_LPAREN	mega_expression	OP_RPAREN	if_gotoF_quadruple	bloque 	fill_if_gotoF2	if_goto_quadruple	ELSE	bloque	fill_if_goto
			
	'''
def p_if_gotoF_quadruple(p):
	' if_gotoF_quadruple	:	epsilon'
	exp_type = stackType.pop()
	if exp_type == 'boolean':
		result = stackOP.pop()
		quadruples.append(['gotoF', result, '', ''])
		stackJumps.append(len(quadruples) -1) # el -1 porque el primer elemnto del quadruplo esta en el index 0
	else:
		print ("Type mismatch error at line  " + str(p.lexer.lineno), ', if without a boolean parameter')
		quit()


def p_fill_if_gotoF1(p):
	'fill_if_gotoF1	:	epsilon'
	if_end = stackJumps.pop()
	quadruples[if_end][3] = len(quadruples) 	

# Se le suma mas uno porque cuando un if lleva un else se genera un cuadruplo goto y es un brinco mas ( +1)
def p_fill_if_gotoF2(p):
	'fill_if_gotoF2	:	epsilon'
	if_end = stackJumps.pop()
	quadruples[if_end][3] = len(quadruples) + 1 # Este mas uno fue el motivo de que sean dos gotoF

def p_fill_if_goto(p):
	'fill_if_goto	:	epsilon'
	if_end = stackJumps.pop()
	quadruples[if_end][3] = len(quadruples) 

def p_if_goto_quadruple(p):
	'if_goto_quadruple	:	epsilon'
	quadruples.append(['goto', '','',''])
	stackJumps.append(len(quadruples)-1)
def p_printer(p):
	'''
	printer	:	PRINT	OP_LPAREN	impression	OP_RPAREN	 SEMICOLON

	'''
def	p_impression(p):
	'''
	impression	:	mega_expression 	printer_quadruple
				|	mega_expression		printer_quadruple	COMA		impression
	'''

def p_printer_quadruple(p):
	'printer_quadruple	:	epsilon'
	left_op = stackOP.pop()
	left_type = stackType.pop() # Quien sabe si esto no sirva pero aqui lo guarde

	quadruples.append(['print', left_op, '',''])
	 
def p_increment(p):
	'''
	increment	:	ID	push_varID_to_Stack		OP_PLUS_EQUALS 		push_symbol			mega_expression		increment_equals		SEMICOLON
				|	ID	push_varID_to_Stack		OP_MINUS_EQUALS	 	push_symbol			mega_expression		increment_equals		SEMICOLON
				|	ID	push_varID_to_Stack		OP_PLUS				OP_PLUS				incrementByOne		SEMICOLON
				|	ID	push_varID_to_Stack		OP_MINUS			OP_MINUS			incrementByOne		SEMICOLON
	'''

def p_incrementByOne(p):
	'incrementByOne		:	epsilon'
	left_op = stackOP.pop()
	left_type = stackType.pop()
	typeResult = VCsemantics.validateSemanticCube(p[-1],left_type, 'int')  # asumimos que 1 = 'int'
	
	if typeResult != 'error':
		cteValue, cteType, cteIndexMem = VCsemantics.push_cte_toTable(1, str(p.lexer.lineno))# get index of cte 1
		tempo =  VCmemory.getTempIndex(typeResult)# nos ayuda a conseguir el index de los temporales dependiendo del tipo
		quadruples.append([p[-1], left_op,cteIndexMem,tempo])
		quadruples.append(['=',tempo, '', left_op])
	else:
		print ("Type mismatch error at line  " + str(p.lexer.lineno))
		quit()

def p_increment_equals(p):
	'increment_equals	:	epsilon'

	right_op = stackOP.pop()
	right_type = stackType.pop()
	left_op = stackOP.pop()
	left_type = stackType.pop()
	operator = stackSymbol.pop()
	if operator =='+=':
		operator = '+'
	else:
		operator = '-'

	typeResult = VCsemantics.validateSemanticCube(operator, left_type, right_type)
	if typeResult != 'error':
		tempo =  VCmemory.getTempIndex(typeResult)
		quadruples.append([operator, left_op, right_op, tempo])
		quadruples.append(['=', tempo, ' ', left_op])


def p_for(p):
	'''
	for	:	FOR		OP_LPAREN	assigment loop_jumpCount		mega_expression	SEMICOLON loop_gotoF	increment	OP_RPAREN	bloque	loop_fill
	'''

def p_while_loop(p):
	'''
	while_loop		:	WHILE	loop_jumpCount		OP_LPAREN	mega_expression OP_RPAREN  loop_gotoF	bloque		loop_fill

	'''
def p_loop_jumpCount(p):
	'loop_jumpCount	:	epsilon'
	stackJumps.append(len(quadruples) -1)
	
def p_loop_gotoF(p):
	'loop_gotoF	:	epsilon'
	type_result = stackType.pop()
	if type_result == 'boolean':
		result = stackOP.pop()
		quadruples.append(['gotoF', result, '',''])
		stackJumps.append(len(quadruples)-1)
	else:
		print ("Type mismatch error at line  " + str(p.lexer.lineno), ', if without a boolean parameter')
		quit()
def p_loop_fill(p):
	'loop_fill		:	epsilon'
	end = stackJumps.pop()
	retorno = stackJumps.pop()
	quadruples.append(['goto', '','',retorno + 1]) # regresa a la condicion de while
	quadruples[end][3]= len(quadruples) # rellena el gotoF del while
def p_return(p):
	'''
	return	:	RETURN 	mega_expression  return_quadruple	SEMICOLON
	'''

def p_return_quadruple(p):
	'return_quadruple	:	epsilon'

	functionType = VCsemantics.getFunctionType(len(VCsemantics.functionDir))
	param = stackOP.pop()
	paramType = stackType.pop()
	
	if functionType == 'void':
		print ("ERROR: A return in a void function at line  " + str(p.lexer.lineno))
		quit()
	elif functionType != paramType:
		print ("ERROR: return type is diferent from function type  " + str(p.lexer.lineno))
		quit()
	else:
		quadruples.append(['return', param, '',''])


def p_function_call(p):
	'''
	function_call :	ID	create_era	OP_LPAREN	function_call_parameters	OP_RPAREN  create_gosub	SEMICOLON
	'''
def p_function_call_parameters(p):
	'''
	function_call_parameters	:	mega_expression	create_param	function_call_parameters_prime
								|	epsilon
	'''

def p_function_call_parameters_prime(p):
	'''
	function_call_parameters_prime		:	COMA	mega_expression create_param  function_call_parameters_prime
										|	epsilon
	'''

def p_create_era(p):
	'create_era		:	epsilon'
	global functionIndex_onCall 
	if VCsemantics.checkIfFunctionExists(p[-1]): 
		quadruples.append(['era', p[-1], '',''])
		functionIndex_onCall = VCsemantics.returnFunctionIndex(p[-1])
	else: 
		print('The function', p[-1], 'at line', str(p.lexer.lineno), 'does not exist')
		quit()

def p_create_param(p):
	'create_param	:	epsilon'
	global param_counter, functionIndex_onCall
	param_counter += 1

	param = stackOP.pop() 
	paramType = stackType.pop()
	if VCsemantics.validateFunctionParams(functionIndex_onCall, param_counter, paramType,  str(p.lexer.lineno)):
		quadruples.append(['param', param, '', 'param' + str(param_counter)])
	else:
		print('TypeError: validateFunctionParams() at line ',  str(p.lexer.lineno))
		quit()
		
def p_create_gosub(p):
	'create_gosub	:	epsilon'
	global param_counter, functionIndex_onCall

	functionName = VCsemantics.getFunctionName(functionIndex_onCall)
	functionParamas = VCsemantics.returnFunctionParamNumbers(functionIndex_onCall)

	if param_counter != functionParamas:
		print('TypeError: validateFunctionParams() at line ',  str(p.lexer.lineno))
		quit()
	else:
		quadruples.append(['gosub', functionName, '', ''])

		#resetear las variables globales
		param_counter = 0
		functionIndex_onCall = 0




def p_mega_expression(p):
	'''
	mega_expression	:	super_expression	check_symbol_megaexp
					|	super_expression	AND		push_symbol		super_expression	check_symbol_megaexp
					|	super_expression	OR		push_symbol		super_expression	check_symbol_megaexp
	'''

def p_check_symbol_megaexp(p):
	'check_symbol_megaexp		:		epsilon'
	if stackSymbol: # Si el stack no esta vacio
		
		if stackSymbol[-1] == 'and' or stackSymbol[-1] == 'or':
			right_op = stackOP.pop()
			right_type = stackType.pop()
			left_op = stackOP.pop()
			left_type = stackType.pop()
			operator = stackSymbol.pop()
			typeResult = VCsemantics.validateSemanticCube(operator ,left_type, right_type)  # si al sumar dos enteros se regresa un entero typeresult es = 'int'
			tempo =  VCmemory.getTempIndex(typeResult)
			if typeResult != 'error': # si sumas un entero con un string typeresult seria = a 'error'
				quadruples.append([operator,left_op, right_op, tempo])
				stackOP.append(tempo)
				stackType.append(typeResult)
				
			else:
				print ("Type mismatch error at line  " + str(p.lexer.lineno))
				quit()

def p_super_expression(p):
	'''
	super_expression	:	expression		check_symbol_superexp
						|	expression		OP_GREATER_THAN			 push_symbol	expression	check_symbol_superexp
						|	expression		OP_LESS_THAN			 push_symbol	expression	check_symbol_superexp
						|	expression		OP_GREATER_EQUALS_THAN	 push_symbol	expression	check_symbol_superexp
						|	expression		OP_LESS_EQUALS_THAN		 push_symbol	expression	check_symbol_superexp
						|	expression		OP_EQUALS_TWO			 push_symbol	expression	check_symbol_superexp
						|	expression		OP_NOT_EQUALS			 push_symbol	expression	check_symbol_superexp

	'''
def p_check_symbol_superexp(p):
	'check_symbol_superexp		:	epsilon'
	if stackSymbol: # Si el stack no esta vacio
		
		if stackSymbol[-1] == '>' or stackSymbol[-1] == '<'  or stackSymbol[-1] == '<='  or stackSymbol[-1] == '>='  or stackSymbol[-1] == '=='  or stackSymbol[-1] == '!=':
			right_op = stackOP.pop()
			right_type = stackType.pop()
			left_op = stackOP.pop()
			left_type = stackType.pop()
			operator = stackSymbol.pop()
			typeResult = VCsemantics.validateSemanticCube(operator ,left_type, right_type)  # si al sumar dos enteros se regresa un entero typeresult es = 'int'
			tempo =  VCmemory.getTempIndex(typeResult)
			if typeResult != 'error': # si sumas un entero con un string typeresult seria = a 'error'
				quadruples.append([operator,left_op, right_op, tempo])
				stackOP.append(tempo)
				stackType.append(typeResult)
				
			else:
				print ("Type mismatch error at line  " + str(p.lexer.lineno))
				quit()
def p_expression(p): 
	'''
	expression :	term	check_symbol_exp
				|	term	check_symbol_exp	OP_PLUS		push_symbol		expression	
				|	term	check_symbol_exp	OP_MINUS	push_symbol		expression	
				
	'''
	
def p_push_symbol(p):
	'push_symbol	:	epsilon'
	stackSymbol.append(p[-1])

def p_check_symbol_exp(p):
	'check_symbol_exp	:	epsilon'

	if stackSymbol: # Si el stack no esta vacio
		
		if stackSymbol[-1] == '+' or stackSymbol[-1] == '-':
			right_op = stackOP.pop()
			right_type = stackType.pop()
			left_op = stackOP.pop()
			left_type = stackType.pop()
			operator = stackSymbol.pop()
			typeResult = VCsemantics.validateSemanticCube(operator ,left_type, right_type)  # si al sumar dos enteros se regresa un entero typeresult es = 'int'
			tempo =  VCmemory.getTempIndex(typeResult)
			if typeResult != 'error': # si sumas un entero con un string typeresult seria = a 'error'
				quadruples.append([operator,left_op, right_op, tempo])
				stackOP.append(tempo)
				stackType.append(typeResult)
				
			else:
				print ("Type mismatch error at line  " + str(p.lexer.lineno))
				quit()
			
def p_term(p):
	'''
	term	:	fact	check_symbol_term
			|	fact	check_symbol_term	OP_DIVISION		push_symbol		term	
			|	fact	check_symbol_term	OP_TIMES		push_symbol		term	

	'''
def p_check_symbol_term(p):
	'check_symbol_term	:	epsilon'
	
	if stackSymbol: # Si el stack no esta vacio
	
		if stackSymbol[-1] == '*' or stackSymbol[-1] == '/':

			right_op = stackOP.pop()
			right_type = stackType.pop()

			left_op = stackOP.pop()
			left_type = stackType.pop()

			operator = stackSymbol.pop()

			typeResult = VCsemantics.validateSemanticCube(operator,left_type, right_type)  # si al sumar dos enteros se regresa un entero typeresult es = 'int'
			tempo =  VCmemory.getTempIndex(typeResult)
			if typeResult != 'error': # si sumas un entero con un string typeresult seria = a 'error'
				quadruples.append([operator,left_op, right_op, tempo])
				stackOP.append(tempo)
				stackType.append(typeResult)
			
			else:
				print ("Type mismatch error at line  " + str(p.lexer.lineno))
				quit()
def p_fact(p):
	'''
	fact	:	var_cte			
			|	OP_LPAREN		push_bottle_bottom		mega_expression		OP_RPAREN		remove_bottle_bottom
	'''
def p_push_varID_to_Stack(p):
	'push_varID_to_Stack	:	epsilon'
	# Con validateIdScope sabemos a que scope pertenece las variables a meter a la pila junto con su tipo
	varName, varType,  varMemIndex = VCsemantics.validateIDScope(p[-1] , str(p.lexer.lineno)) 
	#stackOP.append(varMemIndex) # quitar comments para mostrar memindex
	stackOP.append(varName) # quitar comments para mostrar nombre de var
	stackType.append(varType)


def p_push_bottle_bottom(p):
	'push_bottle_bottom	:	epsilon'
	stackSymbol.append(p[-1])

def p_remove_bottle_bottom(p):
	'remove_bottle_bottom	:	epsilon'
	stackSymbol.pop()

def p_var_cte(p):
	'''
	var_cte : 	ID			push_varID_to_Stack
			| 	VAR_INT		push_cte_toTable
			|	VAR_FLOAT	push_cte_toTable
			|	VAR_STRING	push_cte_toTable
			|	VAR_BOOLEAN	push_cte_toTable
	'''
	p[0] = p[1]

def p_push_cte_toTable(p):
	'push_cte_toTable	:	epsilon'
	
	cteValue, cteType, cteIndexMem = VCsemantics.push_cte_toTable(p[-1], str(p.lexer.lineno))
	#stackOP.append(cteIndexMem)# muestra memIndex
	stackOP.append(cteValue)# muestra los valores, mas facil para debugear
	stackType.append(cteType) 
def p_fun_esp(p):
	'''
	fun_esp		:	figure_creation
	'''
def p_figure_creation(p):
	'''
	figure_creation		:	FIGURE	ID	OP_TWO_POINTS	figure	POSSESS		bloque_figura
	'''
def p_figure(p):
	'''
	figure	:	POINT
			|	LINE
			|	SQUARE
			|	RECTANGLE
			|	TRIANGLE
			|	CIRCLE
			|	ARC
	'''
def p_bloque_figura(p):
	'''
	bloque_figura	:	LCURLY_BRACKET	bloque_figura_primo	RCURLY_BRACKET	
	
	'''

def p_bloque_figura_primo(p):
	'''
	bloque_figura_primo	:	bloque_figura_primo		figura_attr
						|	epsilon
			
	'''	
def p_figura_attr(p):
	'''
	figura_attr	:	vector
				|	COLOR	OP_TWO_POINTS	ID	SEMICOLON
				|	SIZE	OP_TWO_POINTS	mega_expression	SEMICOLON
	'''
def p_vector(p):
	'''
	vector	:	VECTOR		ID		OP_TWO_POINTS		OP_LPAREN	mega_expression	COMA	mega_expression	OP_RPAREN	SEMICOLON
	'''


def p_epsilon(p):
	'epsilon : '
	p[0] = None


def p_error(p):
	print ("Syntax error at line " + str(p.lexer.lineno) + " Unexpected token  " + str(p.value))
	sys.exit(0)

def parsing():
	##### Reading the input from a file#################3
	parser = yacc.yacc()
	f = open('test.txt', 'r').read()
	result = parser.parse(f)	
	print(result)


def printing_quadruples():
	print('Quadruples:')
	index = 0
	for quadruple in quadruples:
		print(index, quadruple)
		index +=1

def printing_varTable():
	print('VarTable: [index, name, Type,  memIndex]')
	for element in VCsemantics.varsTable:
		print(element)

def printFunctionDir():
	print('Function Directory:  [index, name, returnType, firstQuadruple, #parameters, #variables]')
	
	for element in VCsemantics.functionDir:
		print(element)

def printfunctionSignature():
	print('Function Signature:  ')
	for element in VCsemantics.functionSignature:
		print(element)

def printCteTable():
	print('CTE Table: [index, value, Type, memIndex]')
	for element in VCsemantics.cteTable:
		print(element)

def getTypesQty():
	VCmemory.getContextTypesQty() # genera la lista con la cantidad de los tipos en los contextos
	VCmemory.cteTypeQty.append(['cte', VCsemantics.indexCtelInt - 40001, VCsemantics.indexCteFloat - 43001,
								VCsemantics.indexCteString - 46001, VCsemantics.indexCteBoolean - 48001])
	print(VCmemory.globalVarTypeQty)
	print(VCmemory.localVarTypeQty)
	print(VCmemory.cteTypeQty)


def main():
	print('')
	parsing()
	print('')
	printFunctionDir()
	print('')
	printfunctionSignature()
	print('')
	printing_varTable()
	print('')
	printCteTable()
	print('')
	printing_quadruples()
	print('')
	#print('pila Operadores:' , stackOP)
	#print('pila de tipos:' ,stackType)
	#print('pila de simbolos:' ,stackSymbol)
	getTypesQty()

	
	
	


	

if __name__ == '__main__':
    main()
	


'''
##########Reading the input from the terminal#############
while True: #Passing the input to the parser
	try:
		s= input()
	except EOFError:
		break
	#if not s: continue
	result = parser.parse(s)
	#print(result)
'''	




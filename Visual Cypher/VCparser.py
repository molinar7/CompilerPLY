import VCscanner as lexer
import ply.yacc as yacc
import sys
import VCsemantics
from VCquadruples import * # con esto ya no es necesario poner el nombre de la clase
import VCmemory


tokens = lexer.tokens
tmp_type = ''

def p_program(p):
	'''
	program		:	PROGRAM  ID  LCURLY_BRACKET  vars   function 	main_function	 RCURLY_BRACKET	

	'''
	p[0] = "Syntax Accepted!"


def p_vars(p):
	'''
	vars	:	type	save_type	ID		OP_EQUALS			var_cte_VARS	pushTo_varsTable_WithCTE	SEMICOLON		vars
			|	type	save_type	ID		pushTo_varsTable	vars_prime		SEMICOLON					vars
			|	epsilon
	'''
def p_vars_prime(p):
	'''
	vars_prime		:	COMA	ID	pushTo_varsTable	vars_prime
					|	epsilon
	'''



def p_pushTo_varsTable_WithCTE(p):
	'pushTo_varsTable_WithCTE	:	epsilon'
	VCsemantics.pushTo_varsTable_WithCTE(p[-3], tmp_type, p[-1], str(p.lexer.lineno))

def p_pushTo_varsTable(p):
	'pushTo_varsTable	:	epsilon'
	VCsemantics.pushTo_varsTable(p[-1], tmp_type, str(p.lexer.lineno))
	

def p_save_type(p):
	'save_type	:	epsilon'
	global tmp_type
	tmp_type = p[-1]
	
def p_function(p):
	'''
	function	:	FUNCTION	type	ID		pushTo_FunctionDir		OP_LPAREN		parameters OP_RPAREN	function_bloque	function
				|	FUNCTION	VOID	ID		pushTo_FunctionDir		OP_LPAREN		parameters OP_RPAREN	function_bloque	function
				|	epsilon
	'''
def p_pushTo_FunctionDir(p):
	'''
	pushTo_FunctionDir	:	epsilon
	'''
	VCsemantics.pushTo_FunctionDir(p[-1],p[-2], str(p.lexer.lineno))

def p_main_function(p):
	'''
	main_function	:	MAIN	pushTo_FunctionDir OP_LPAREN	OP_RPAREN	function_bloque	
	'''
def p_type(p):
	'''
	type	:	INT
			|	FLOAT
			|	STRING
			|	BOOLEAN
			
	'''
	p[0] = p[1]
def p_parameters(p):
	'''
	parameters	:	type		ID			parameters
				|	COMA		type		ID				parameters
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
		#stackOP.append(left_op) 
		#stackType.append(left_type)
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
	return	:	RETURN 	mega_expression 	SEMICOLON
	'''
def p_function_call(p):
	'''
	function_call :	ID	OP_LPAREN	function_call_prime		OP_RPAREN	SEMICOLON
	'''
def p_function_call_prime(p):
	'''
	function_call_prime	:	ID		function_call_prime
						|	COMA	ID		function_call_prime
						|	epsilon
	'''


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
	varName, varType, varValue, varMemIndex = VCsemantics.validateIDScope(p[-1] , str(p.lexer.lineno)) 
	stackOP.append(varMemIndex) # quitar comments para mostrar memindex
	#stackOP.append(varName) # quitar comments para mostrar nombre de var
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
			|	VAR_BOOLEAN
	'''
	p[0] = p[1]

def p_push_cte_toTable(p):
	'push_cte_toTable	:	epsilon'
	
	cteValue, cteType, cteIndexMem = VCsemantics.push_cte_toTable(p[-1], str(p.lexer.lineno))
	stackOP.append(cteIndexMem)# muestra memIndex
	#stackOP.append(cteValue)# muestra los valores, mas facil para debugear
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
def p_var_cte_VARS(p): # Esta regla nomas se usa para la asignacion al definir variables
	'''
	var_cte_VARS 	: 	ID			
					| 	VAR_INT		
					|	VAR_FLOAT	
					|	VAR_STRING	
					|	VAR_BOOLEAN
	'''
	p[0] = p[1]

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

def main():
	parsing()
	print ('FunctionDir:', VCsemantics.functionDir)
	print('VarTable:', VCsemantics.varsTable)
	print('cteTable:', VCsemantics.cteTable)
	printing_quadruples()
	print('pila Operadores:' , stackOP)
	print('pila de tipos:' ,stackType)
	print('pila de simbolos:' ,stackSymbol)

	

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




import VCscanner as lexer
import ply.yacc as yacc
import sys
import VCsemantics

tokens = lexer.tokens
tmp_type = ''

def p_program(p):
	'''
	program		:	PROGRAM  ID  LCURLY_BRACKET  vars   function 	main_function	 RCURLY_BRACKET	

	'''
	p[0] = "Syntax Accepted!"


def p_vars(p):
	'''
	vars	:	type	save_type	ID		OP_EQUALS			var_cte			pushTo_varsTable_WithCTE	SEMICOLON		vars
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
	VCsemantics.pushTo_varsTable_WithCTE(p[-3], tmp_type, p[-1])

def p_pushTo_varsTable(p):
	'pushTo_varsTable	:	epsilon'
	VCsemantics.pushTo_varsTable(p[-1], tmp_type)
	

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
	VCsemantics.pushTo_FunctionDir(p[-1],p[-2])

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
				
	'''

def p_assigment(p):
	'''
	assigment	:	ID	OP_EQUALS	single_expression	SEMICOLON
				|	ID	OP_LSQUARE_PAREN	VAR_INT		OP_RSQUARE_PAREN	OP_EQUALS	single_expression	

	'''
def p_if (p):
	'''
	if	:	IF	OP_LPAREN	condition_mega_expression	OP_RPAREN	bloque
		|	IF	OP_LPAREN	condition_mega_expression	OP_RPAREN	bloque		ELSE	bloque	
			
	'''


def p_printer(p):
	'''
	printer	:	PRINT	OP_LPAREN	impression	OP_RPAREN	 SEMICOLON

	'''
def	p_impression(p):
	'''
	impression	:	mega_expression
				|	mega_expression		OP_PLUS		impression
	
	'''
def p_increment(p):
	'''
	increment	:	ID	OP_PLUS_EQUALS 		single_expression		SEMICOLON
				|	ID	OP_MINUS_EQUALS	 	single_expression		SEMICOLON
				|	ID	OP_PLUS				OP_PLUS				SEMICOLON
				|	ID	OP_MINUS			OP_MINUS			SEMICOLON
	'''
	
def p_for(p):
	'''
	for	:	FOR		OP_LPAREN	assigment	condition_super_expression	SEMICOLON	increment	OP_RPAREN	bloque	
	'''

def p_return(p):
	'''
	return	:	RETURN 	single_expression 	SEMICOLON
	'''
def p_function_call(p):
	'''
	function_call :	ID	OP_LPAREN	function_call_prime		OP_RPAREN	SEMICOLON
	'''
def p_function_call_prime(p):
	'''
	function_call_prime	:	ID		function_call_prime
						|	COMA	ID						function_call_prime
						|	epsilon
	'''
def p_condition_mega_expression(p):
	'''
	condition_mega_expression	:	condition_super_expression
								|	condition_super_expression	AND		condition_super_expression
								|	condition_super_expression	OR		condition_super_expression
	'''
def p_condition_super_expression(p):
	'''
	condition_super_expression	:	expression	OP_GREATER_THAN			 expression
								|	expression	OP_LESS_THAN			 expression
								|	expression	OP_GREATER_EQUALS_THAN	 expression
								|	expression	OP_LESS_EQUALS_THAN		 expression
								|	expression	OP_EQUALS_TWO			 expression
								|	expression	OP_NOT_EQUALS			 expression
	'''
	# Estos single_ son usadas en assigments e increments para evitar operadores no deseados e. <=
def p_single_expression(p): 
	'''
	single_expression 	:	single_term
						|	single_term		OP_PLUS		single_expression	
						|	single_term		OP_MINUS	single_expression				
	'''
def p_single_term(p):
	'''
	single_term	:	single_fact
				|	single_fact	OP_DIVISION		single_term	
				|	single_fact	OP_TIMES		single_term	

	'''
def p_single_fact(p):
	'''
	single_fact	:	var_cte
				|	OP_LPAREN		single_expression		OP_RPAREN	
	'''
def p_mega_expression(p):
	'''
	mega_expression	:	super_expression
					|	super_expression	AND		super_expression
					|	super_expression	OR		super_expression
	'''

def p_super_expression(p):
	'''
	super_expression	:	expression
						|	expression	OP_GREATER_THAN			 expression
						|	expression	OP_LESS_THAN			 expression
						|	expression	OP_GREATER_EQUALS_THAN	 expression
						|	expression	OP_LESS_EQUALS_THAN		 expression
						|	expression	OP_EQUALS_TWO			 expression
						|	expression	OP_NOT_EQUALS			 expression

	'''
def p_expression(p): 
	'''
	expression :	term
				|	term	OP_PLUS		expression	
				|	term	OP_MINUS	expression	
				
	'''

def p_term(p):
	'''
	term	:	fact
			|	fact	OP_DIVISION		term	
			|	fact	OP_TIMES		term	

	'''
def p_fact(p):
	'''
	fact	:	var_cte
			|	OP_LPAREN		mega_expression		OP_RPAREN	
	'''
def p_var_cte(p):
	'''
	var_cte : 	ID
			| 	VAR_INT
			|	VAR_FLOAT
			|	VAR_STRING
	'''
	p[0] = p[1]
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
				|	SIZE	OP_TWO_POINTS	single_expression	SEMICOLON
	'''
def p_vector(p):
	'''
	vector	:	VECTOR		ID		OP_TWO_POINTS		OP_LPAREN	single_expression	COMA	single_expression	OP_RPAREN	SEMICOLON
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

def main():
	parsing()
	print (VCsemantics.functionDir)
	print(VCsemantics.varsTable)

	

	



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




import VCscanner as lexer
import ply.yacc as yacc
import sys

tokens = lexer.tokens

def p_program(p):
	'''
	program		:	PROGRAM  ID  LCURLY_BRACKET  vars   function 	main_function	 RCURLY_BRACKET	

	'''
	p[0] = "Syntax Accepted!"

def p_vars(p):
	'''
	vars	:		INT	 	 ID		OP_EQUALS	VAR_INT	 	SEMICOLON	vars
			|		FLOAT	 ID		OP_EQUALS	VAR_FLOAT 	SEMICOLON	vars
			|		STRING	 ID		OP_EQUALS	VAR_STRING	SEMICOLON	vars
			|		BOOLEAN	 ID		OP_EQUALS	VAR_BOOLEAN	SEMICOLON	vars
			|		epsilon
	'''
def p_function(p):
	'''
	function	:	FUNCTION	type	ID		OP_LPAREN	parameters OP_RPAREN	bloque	function
				|	epsilon
	'''
def p_main_function(p):
	'''
	main_function	:	MAIN	OP_LPAREN	OP_RPAREN	bloque	
	'''
def p_type(p):
	'''
	type	:	INT
			|	FLOAT
			|	STRING
			|	BOOLEAN
			|	VOID
	'''
def p_parameters(p):
	'''
	parameters	:	type	ID	parameters
				|	COMA	type	ID		parameters
				|	epsilon
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
				|	vars
				|	for
				|	return
				|	function_call
				
	'''

def p_assigment(p):
	'''
	assigment	:	ID	OP_EQUALS	mega_expression		SEMICOLON

	'''
def p_if (p):
	'''
	if	:	IF	OP_LPAREN	mega_expression	OP_RPAREN	bloque
		|	IF	OP_LPAREN	mega_expression	OP_RPAREN	bloque	ELSE	bloque	
			
	'''


def p_printer(p):
	'''
	printer	:	PRINT	OP_LPAREN	impression	OP_RPAREN	 SEMICOLON

	'''
def	p_impression(p):
	'''
	impression	:	var_cte
				|	var_cte		OP_PLUS		impression
	
	'''
def p_increment(p):
	'''
	increment	:	ID	OP_PLUS_EQUALS mega_expression	SEMICOLON
				|	ID	OP_MINUS_EQUALS mega_expression	SEMICOLON
				|	ID	OP_PLUS		OP_PLUS		SEMICOLON
				|	ID	OP_MINUS	OP_MINUS	SEMICOLON
	'''
def p_for(p):
	'''
	for	:	FOR		OP_LPAREN	vars	mega_expression		SEMICOLON	increment	OP_RPAREN	bloque	
	'''

def p_return(p):
	'''
	return	:	RETURN	ID SEMICOLON
			|	RETURN mega_expression SEMICOLON
	'''
def p_function_call(p):
	'''
	function_call :	ID	OP_LPAREN	function_call_prime		OP_RPAREN	SEMICOLON
	'''
def p_function_call_prime(p):
	'''
	function_call_prime	:	ID	function_call_prime
						|	COMA	ID	function_call_prime
						|	epsilon
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
			|	OP_LPAREN	mega_expression	OP_RPAREN	
	'''
def p_var_cte(p):
	'''
	var_cte : 	ID
			| 	VAR_INT
			|	VAR_FLOAT
			|	VAR_STRING
	'''

def p_epsilon(p):
	'epsilon : '
	p[0] = None


def p_error(p):
	print ("Syntax error at line " + str(p.lexer.lineno) + " Unexpected token  " + str(p.value))
	sys.exit(0)


##### Reading the input from a file#################3
parser = yacc.yacc()
f = open('test.txt', 'r').read()
result = parser.parse(f)	
print(result)



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




import VCscanner as lexer
import ply.yacc as yacc
import sys

tokens = lexer.tokens

def p_program(p):
	'''
	program		:	PROGRAM		ID		vars	bloque

	'''
	p[0] = "Syntax Accepted!"

def p_vars(p):# NO valida que enteros en realidad se guarden en int y decimales en floats y letras en Strings
	'''
	vars	:	VAR		type	 ID		OP_EQUALS	ID	 SEMICOLON 
	'''

def p_type(p):
	'''
	type	:	INT
			|	FLOAT
	'''

def p_bloque(p):
	'''
	bloque	:	LCURLY_BRACKET	statement	RCURLY_BRACKET		
	'''
def	p_statement(p):
	'''
	statement	:	mega_expression
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
	fact	:	ID
			|	FLOAT
			|	INT
			|	OP_LPAREN	super_expression	OP_RPAREN	
	'''

def p_printer(p):
	'''
	printer	:	PRINT	OP_LPAREN	QUOT_MARK	ID	QUOT_MARK		OP_RPAREN

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




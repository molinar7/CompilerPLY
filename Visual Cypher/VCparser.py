import VCscanner as lexer
import ply.yacc as yacc
import sys


tokens = lexer.tokens

def p_cal(p): # expression is a non terminal
	'''
	cal :	expression 
		|	epsilon
	'''

	print(p[1])

def p_expression(p): # INT and FLOAT are tokens or terminalss
	'''
	expression :	INT
				|	FLOAT
				
	'''

	p[0] = p[1]

def p_epsilon(p):
	'epsilon : '
	p[0] = None


def p_error(p):
	print ("Syntax error at line " + str(p.lexer.lineno) + " Unexpected token  " + str(p.value))
	sys.exit(0)

#lexer.input(file.read()) # lexer reading some input

parser = yacc.yacc()
while True: #Passing the input to the parser
  try:
  	s= input('')
  except EOFError:
    break
  parser.parse(s)  
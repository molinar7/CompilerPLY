import ply.lex as lex
import sys


#file = open('test.txt', 'r') 



######################LIST OF TOKENS###################################
tokens = [
'ID',
# types of numbers
'FLOAT',
'INT',
#Symbols
'CARET',
'POINT',
'LPAREN',
'RPAREN',
'EQUALS'
]
########################## Reserver Words ####################################################
reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE'
   
}

################### Regular expression rules for simple tokens###########################
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ignore = ' \t' #Ignore spaces and tabs.
t_ignore_COMMENT = r'\#.*'
t_CARET= r'\^'
t_POINT= r'\.'
t_EQUALS= r'\='


############## A regular expression rule with some action code########################
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

 

def t_newline(t): # Define a rule so we can track line numbers
    r'\n+'
    t.lexer.lineno += len(t.value)
    

def t_FLOAT (t):# above the int define so the '.' is not an ilegal char
	r'\d*\.\d+' # integer then a dot followed by 1 or more integers
	t.value = float(t.value)
	return t

def t_INT (t): # Function for defining our INT token
	r'\d+' #d means any integer and the + means 1 or more
	t.value = int(t.value)
	return t

def t_error(t): # Error handling rule
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#############################Building a lexer#######################################
lexer = lex.lex() 


''' ##################Removing the input from the user########3
lexer.input(file.read()) # lexer reading some input


####TOKENIZE##########
while True:
	tok = lexer.token()

	if not tok:
		break	#nomore input
	print(tok)

###########################################################

'''

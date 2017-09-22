import ply.lex as lex
import sys


#file = open('test.txt', 'r') 

######################LIST OF TOKENS###################################
tokens = [

'PROGRAM',
'ID',

# types of numbers
'FLOAT',
'INT',

#Symbols
'CARET',
'POINT',

##Operadores###
'OP_PLUS',
'OP_MINUS',
'OP_TIMES',
'OP_DIVISION',
'OP_EQUALS_TWO',
'OP_NOT_EQUALS',
'OP_LPAREN',
'OP_RPAREN',
'OP_EQUALS',
'OP_LESS_THAN',
'OP_LESS_EQUALS_THAN',
'OP_GREATER_THAN',
'OP_GREATER_EQUALS_THAN',
'AND',
'OR',
'PRINT',
'QUOT_MARK',
'SEMICOLON',
'LCURLY_BRACKET',
'RCURLY_BRACKET',
'VAR'


]

########################## Reserver Words ####################################################
reserved = {


    #Basic tokens
    'program' : 'PROGRAM',
    'var'   :   'VAR',
    'print' : 'PRINT',

    # Condition tokens
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'and' : 'AND',
    'or' : 'OR',

    # Cycle tokens
    'while'      : 'WHILE',
    'for'       : 'FOR',
    
    # Type declaration tokens
    'boolean'   : 'BOOLEAN',
    'int'       : 'INT',
    'float'   : 'FLOAT'
   
}

################### Regular expression rules for simple tokens###########################


t_OP_PLUS = r'\+'
t_OP_MINUS = r'\-'
t_OP_TIMES = r'\*'
t_OP_DIVISION = r'\/'
t_OP_EQUALS_TWO= r'\=='
t_OP_NOT_EQUALS= r'\!='
t_OP_LPAREN  = r'\('
t_OP_RPAREN  = r'\)'
t_OP_EQUALS= r'\='
t_OP_LESS_THAN = r'\<'
t_OP_LESS_EQUALS_THAN = r'\<='
t_OP_GREATER_THAN = r'\>'
t_OP_GREATER_EQUALS_THAN=  r'\>='
t_ignore = ' \t' #Ignore spaces and tabs.
t_ignore_COMMENT = r'\#.*'
t_CARET= r'\^'
t_POINT= r'\.'
t_QUOT_MARK = r'\"'
t_SEMICOLON = r'\;'
t_LCURLY_BRACKET = r'\{'
t_RCURLY_BRACKET = r'\}'


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
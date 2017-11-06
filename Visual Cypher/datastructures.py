# INITIALIZE DICTIONARIES
type_dict = {
	# Numbers Types
	'void'	  	: 0,
	'boolean'   : 1,
	'int'	   	: 2,
	'string'	: 3,
}


inv_type_dict = {v: k for k, v in type_dict.items()}

operator_dict = { 
	# Operadores normales
	'+'  : 0,
	'-'  : 1,
	'*'  : 2,
	'/'  : 3,
	'==' : 4,
	'!=' : 5,
	'<'  : 6,
	'<=' : 7,
	'>'  : 8,
	'>=' : 9,
	'and': 10,
	'or' : 11,
}
special_operator_dict = { 
	# Operadores especiales, aun faltan de agregar bro o quitar ando con la duda
	'('	 		: 12,
	')'	 		: 13,
	'='	 		: 14,
	'gotof'		: 15,
	'gotot'		: 16,
	'goto'		: 17,
	'return'	: 18,
	'gosub'		: 19,
	'era' 		: 20,
	'param'		: 21,
	'print' 	: 22,
	'FUNCTION'	: 23,
	'MAIN' 		: 24,
	'FOR' 		: 25,
	'VOID' 		: 26,
	'VECTOR' 	: 27,
	'POINT'		: 28,
	'LINE'		: 29,
	'SQUARE'	: 30,
	'RECTANGLE' : 31,
	'TRIANGLE'	: 32,
	'CIRCLE'	: 33,
	'FIGURE'	: 34,
	'POSSESS'	: 35,
	'COLOR'		: 36,
	'SIZE'		: 37,
	'OP_LSQUARE_PAREN' : 38,
	'OP_RSQUARE_PAREN' : 39,
	'ARC'		: 40,
	'WHILE'		: 41,
}

merged_dict = dict(operator_dict, **special_operator_dict)
inv_op_dict = {v: k for k, v in merged_dict.items()}

initializer_dict = {
	# Numbers Types
	0   :   "",			 #void
	1   :   False,	 	 #boolean
	2   :   0,			 #int
	4   :   "",			 #string
}

class Stack(object): #Simula un Stack

	def __init__(self):
		self.values = []
	def isEmpty(self):
		return self.values == []
	def push(self,  value):
		self.values.append(value)
	def pop(self):
		if(len(self.values) > 0):
			return self.values.pop()
		else :
			print("Empty Stack")
	def peek(self):
		if(len(self.values) == 0):
			return None
		else:
			return self.values[len(self.values)-1]
	def size(self):
		return len(self.values)
	def pprint(self):
		print self.values
	def inStack(self, var_name):
		return var_name in self.values


class Queue(object): #Simula un Queue

	def __init__(self):
		self.values = []
	def isEmpty(self):
		return self.values == []
	def enqueue(self, value):
		self.values.insert(0,value)
	def dequeue(self):
		if(len(self.values) > 0):
			return self.values.pop()
		else :
			print("Empty Queue")
	def peek(self):
		return self.values[len(self.values)-1]
	def size(self):
		return len(self.values)
	def pprint(self):
		print self.values
	def inQueue(self, var_name):
return var_name in self.values
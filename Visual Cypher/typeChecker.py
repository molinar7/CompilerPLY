import VCsemantics

def isInt(x):
    if isinstance(x,int):
        return True
    else: 
        return False

def isFloat(x):
    if isinstance(x, float):
        return True
    else: 
        return False

def isString(x):
    if isinstance(x, str):
        return True
    else: 
        return False

def isBoolean(x):
    if x == 'True' or x == 'False':
        return True
    else: 
        return False
        

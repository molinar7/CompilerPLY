import VCsemantics
cuboSemantico = [['int','int','+','int'],['int','int','-','int'],['int','int','*','int'],['int','int','/','int'],['int','int','and','error'], ['int','int','or','error'], ['int','int','<','boolean'], ['int','int','>','boolean'], ['int','int','<=','boolean'], ['int','int','>=','boolean'], ['int','int','==','boolean'], ['int','int','!=','error'],
                 ['int','float','+','int'],['int','float','-','int'],['int','float','*','int'],['int','float','/','int'],['int','float','and','error'], ['int','float','or','error'],  ['int','float','<','error'], ['int','float','>','error'], ['int','float','<=','error'], ['int','float','>=','error'], ['int','float','==','error'], ['int','float','!=','error'],
                 ['int','String','+','error'],['int','String','-','error'],['int','String','*','error'],['int','String','/','error'],['int','String','and','error'], ['int','String','or','error'], ['int','String','<','error'], ['int','String','>','error'], ['int','String','<=','error'], ['int','String','>=','error'], ['int','String','==','error'], ['int','String','!=','error'],
                 ['int','boolean','+','error'],['int','boolean','-','error'],['int','boolean','*','error'],['int','boolean','/','error'],['int','boolean','and','error'], ['int','boolean','or','error'], ['int','boolean','<','error'], ['int','boolean','>','error'], ['int','boolean','<=','error'], ['int','boolean','>=','error'], ['int','boolean','==','error'], ['int','boolean','!=','error'],

                 ['float','int','+','float'], ['float','int','-','float'], ['float','int','*','int'], ['float','int','/','int'], ['float','int','and','error'], ['float','int','or','error'], ['float','int','<','error'], ['float','int','>','error'], ['float','int','<=','error'], ['float','int','>=','error'], ['float','int','==','error'], ['float','int','!=','error'],
                 ['float','float','+','float'], ['float','float','-','float'], ['float','float','*','float'], ['float','float','/','float'], ['float','float','and','error'], ['float','float','or','error'], ['float','float','<','boolean'], ['float','float','>','boolean'], ['float','float','<=','boolean'], ['float','float','>=','boolean'], ['float','float','==','boolean'], ['float','float','!=','boolean'],
                 ['float','String','+','error'], ['float','String','-','error'], ['float','String','*','error'], ['float','String','/','error'], ['float','String','and','error'], ['float','String','or','error'], ['float','String','<','error'], ['float','String','>','error'], ['float','String','<=','error'], ['float','String','>=','error'], ['float','String','==','error'], ['float','String','!=','error'],
                 ['float','boolean','+','error'], ['float','boolean','-','error'], ['float','boolean','*','error'], ['float','boolean','/','error'], ['float','boolean','and','error'], ['float','boolean','or','error'], ['float','boolean','<','error'], ['float','boolean','>','error'], ['float','boolean','<=','error'], ['float','boolean','>=','error'], ['float','boolean','==','error'], ['float','boolean','!=','error'],

                 ['String','int','+','error'], ['String','int','-','error'], ['String','int','*','error'], ['String','int','/','error'], ['String','int','and','error'], ['String','int','or','error'], ['String','int','<','error'], ['String','int','>','error'], ['String','int','<=','error'], ['String','int','>=','error'], ['String','int','==','error'], ['String','int','!=','error'],
                 ['String','float','+','error'], ['String','float','-','error'], ['String','float','*','error'], ['String','float','/','error'], ['String','float','and','error'], ['String','float','or','error'], ['String','float','<','error'], ['String','float','>','error'], ['String','float','<=','error'], ['String','float','>=','error'], ['String','float','==','error'], ['String','float','!=','error'],
                 ['String','String','+','error'], ['String','String','-','error'], ['String','String','*','error'], ['String','String','/','error'], ['String','String','and','error'], ['String','String','or','error'], ['String','String','<','error'], ['String','String','>','error'], ['String','String','<=','error'], ['String','String','>=','error'], ['String','String','==','error'], ['String','String','!=','error'],
                 ['String','boolean','+','error'], ['String','boolean','-','error'], ['String','boolean','*','error'], ['String','boolean','/','error'], ['String','boolean','and','error'], ['String','boolean','or','error'], ['String','boolean','<','error'], ['String','boolean','>','error'], ['String','boolean','<=','error'], ['String','boolean','>=','error'], ['String','boolean','==','error'], ['String','boolean','!=','error'],
                #BRO OCUPAMOS VER SI PODREMOS SUMAR LOS STRINGS, POR EL MOMENTO LE PUSE error

                 ['boolean','int','+','error'], ['boolean','int','-','error'], ['boolean','int','*','error'], ['boolean','int','/','error'], ['boolean','int','and','error'], ['boolean','int','or','error'], ['boolean','int','<','error'], ['boolean','int','>','error'], ['boolean','int','<=','error'], ['boolean','int','>=','error'], ['boolean','int','==','error'], ['boolean','int','!=','error'],
                 ['boolean','float','+','error'], ['boolean','float','-','error'], ['boolean','float','*','error'], ['boolean','float','/','error'], ['boolean','float','and','error'], ['boolean','float','or','error'], ['boolean','float','<','error'], ['boolean','float','>','error'], ['boolean','float','<=','error'], ['boolean','float','>=','error'], ['boolean','float','==','error'], ['boolean','float','!=','error'],
                 ['boolean','String','+','error'], ['boolean','String','-','error'], ['boolean','String','*','error'], ['boolean','String','/','error'], ['boolean','String','and','error'], ['boolean','String','or','error'], ['boolean','String','<','error'], ['boolean','String','>','error'], ['boolean','String','<=','error'], ['boolean','String','>=','error'], ['boolean','String','==','error'], ['boolean','String','!=','error'],
                 ['boolean','boolean','+','error'], ['boolean','boolean','-','error'], ['boolean','boolean','*','error'], ['boolean','boolean','/','error'], ['boolean','boolean','and','boolean'], ['boolean','boolean','or','boolean'], ['boolean','boolean','<','error'], ['boolean','boolean','>','error'], ['boolean','boolean','<=','error'], ['boolean','boolean','>=','error'], ['boolean','boolean','==','boolean'], ['boolean','boolean','!=','boolean']

                ]
                
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
        

import typeChecker
import VCquadruples

# Semantic Cube for the + and -
termCube = [['int','int', True],['int','float', True],['int','String', False],['int', 'boolean', False],
            ['float', 'int', True], ['float','float', True], ['float', 'String', False], ['float', 'boolean', False],
            ['String' , 'int', False],['String', 'float', False], ['String', 'String', False], ['String', 'boolean', False],
            ['boolean', 'int', False], ['boolean', 'float', False], ['boolean', 'String', False],['boolean', 'boolean', False]]

 # Semantic cube for the * and /
factCube = [['int','int', True],['int','float', False],['int','String', False],['int', 'boolean', False],
            ['float', 'int', False], ['float','float', True], ['float', 'String', False], ['float', 'boolean', False],
            ['String' , 'int', False],['String', 'float', False], ['String', 'String', False], ['String', 'boolean', False],
            ['boolean', 'int', False], ['boolean', 'float', False], ['boolean', 'String', False],['boolean', 'boolean', False]]

#len(functionDir) nos ayuda a saber en que scope nos ubicamos :)

functionDir = [[1,'global', None]] # El directorio de funciones
varsTable = [] #LA tabla de variables


indexGlobalInt = 100001 # index de la memoria virutal
indexGlobalFloat = 130001
indexGlobalString = 160001
indexGlobalBoolean = 180001

def validate_termCube(x,y):
    for elements in termCube:
        if x == elements[0] and y == elements[1]:
            return elements[2]

def validate_factCube(x,y):
    for elements in factCube:
        if x == elements[0] and y == elements[1]:
            return elements[2]

def pushTo_FunctionDir(n,t, lineno):
    if not checkIfFunctionExists(n):
        functionDir.append([ len(functionDir) + 1, n, t])
    else:
        print('ERROR:', 'The function',n, 'at line:', lineno, 'is already defined')
    

def pushTo_varsTable_WithCTE(n, t, v, lineno): #Append it to the varTable when defining a var with value
    if not checkIfVarIdExistsOnModule(n): # Checa que la vairable no este ya definida en el modulo actual

        if t == 'int':
            if typeChecker.isInt(v):
                if len(functionDir) == 1: # We know that is global if the index is 1
                    global indexGlobalInt
                    varsTable.append([len(functionDir), n, t, v, indexGlobalInt])
                    indexGlobalInt += 1
                else:
                    varsTable.append([len(functionDir), n, t, v, '']) # no le he puesto un index de memoria virtual por dudas
            else:
                print('ERROOR:','The variable',n,'at line', lineno, 'is not a',t)
                quit()
        

        if t == 'float':
            if typeChecker.isFloat(v):
                if len(functionDir) == 1: 
                    global indexGlobalFloat
                    varsTable.append([len(functionDir), n, t, v, indexGlobalFloat])
                    indexGlobalFloat += 1
                else:
                    varsTable.append([len(functionDir), n, t, v, ''])
            else:
                print('ERROR:','The variable',n,'at line', lineno, 'is not a',t)
                quit()


        if t == 'String':
            if typeChecker.isString(v):
                if len(functionDir) == 1:
                    global indexGlobalString
                    varsTable.append([len(functionDir), n, t, v, indexGlobalString])
                    indexGlobalString += 1
                else:
                    varsTable.append([len(functionDir), n, t, v, ''])
            else:
                print('ERROR:','The variable',n,'at line', lineno, 'is not a',t)
                quit()


        if t == 'boolean':
            if typeChecker.isBoolean(v):
                if len(functionDir) == 1:
                    global indexGlobalBoolean
                    varsTable.append([len(functionDir), n, t, v, indexGlobalBoolean])
                    indexGlobalBoolean += 1
                else:
                    varsTable.append([len(functionDir), n, t, v, ''])
            else:
                print('ERROR:','The variable',n,'at line', lineno, 'is not a',t)
                quit()

    else:
        print('ERROR:', 'The variable',n, 'at line', lineno, 'is already defined') 
        quit()
    

def pushTo_varsTable(n, t, lineno ): #Append it to the varTable when defining a var with NOT value
    
    if not checkIfVarIdExistsOnModule(n): # Checa que no exista en el modulo actual la variable
    
        if t == 'int':
            global indexGlobalInt
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t, '', indexGlobalInt])
                indexGlobalInt +=1
            else:
                varsTable.append([len(functionDir), n, t, '',''])

        if t == 'float':
            global indexGlobalFloat
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t,'', indexGlobalFloat])
                indexGlobalFloat +=1
            else:
                varsTable.append([len(functionDir), n, t, '',''])

        if t == 'String':
            global indexGlobalString
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t,'', indexGlobalString])
                indexGlobalString +=1
            else:
                varsTable.append([len(functionDir), n, t, '',''])
        
        if t == 'boolean':
            global indexGlobalBoolean
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t,'', indexGlobalBoolean])
                indexGlobalBoolean +=1
            else:
                varsTable.append([len(functionDir), n, t, '',''])


    else:
        print('ERROR:', 'The variable',n,'at line',  lineno, 'is already defined')  
        quit()
    



def validateIDScope(v, lineno): # Esta funcion nos sirve para ver que scope tiene la id

    if checkIfVarIdExistsOnModule(v): # Se checa si existe primero en el modulo
        print(v,'exist on module')

    else:
        if checkIfVarIdExistsOnGlobal(v):# Se checa si existe despues en las variables globales
            print(v,'exist on global')
            for id in varsTable:
                if id[0] == 1:
                    if id[1] == v:
                        return id[1], id[2],id[4] #  = varName, varType, varMemIndex 
                        



        else:# Si no existe en en modulo ni en las variavles globales pues no esta definida
            print('ERROR:', v, 'at line', lineno ,'does not exist, you need to define it')
            quit()

    
   


def checkIfFunctionExists(n): # check that functions do not repeat
    for nombre in functionDir:
       if n == nombre[1]:
           return True    
    return False  

def checkIfVarIdExistsOnModule(n): # check if Var ID exists on module
    for varID in varsTable:
        
        if len(functionDir) == varID[0]: # Unicamente queremos que busque en su modulo 
            if varID[1] == n:
                return True
    return False

def checkIfVarIdExistsOnGlobal(n): # check if Var ID exists on global
    for varID in varsTable:
        if varID[0] == 1: # Unicamente queremos que busque en las variables globales
            if varID[1] == n:
                return True
    return False
            


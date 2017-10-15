import typeChecker
# Semantic Cube for the + and -
termCube = [['int','int', True],['int','float', True],['int','String', False],['int', 'boolean', False],
            ['float','float', True], ['float', 'String', False], ['float', 'boolean', False],
            ['String', 'String', False], ['String', 'boolean', False],
            ['boolean', 'boolean', False]]

 # Semantic cube for the * and /
factCube = [['int','int', True],['int','float', False],['int','String', False],['int', 'boolean', False],
            ['float','float', True], ['float', 'String', False], ['float', 'boolean', False],
            ['String', 'String', False], ['String', 'boolean', False],
            ['boolean', 'boolean', False]]

#len(functionDir) nos ayuda a saber en que scope nos ubicamos :)
functionDir = [[1,'global', None]]
varsTable = []

indexGlobalInt = 100001
indexGlobalFloat = 130001
indexGlobalString = 160001

def pushTo_FunctionDir(n,t):
    if not checkIfFunctionExists(n):
        functionDir.append([ len(functionDir) + 1, n, t])
    else:
        print('The function',n, 'is already defined')
    

def pushTo_varsTable_WithCTE(n, t, v): #Append it to the varTable when defining a var with value
    if not checkIfVarIdExistsOnModule(n):

        if t == 'int':
            if typeChecker.isInt(v):
                if len(functionDir) == 1: # We know that is global if the index is 1
                    global indexGlobalInt
                    varsTable.append([len(functionDir), n, t, v, indexGlobalInt])
                    indexGlobalInt += 1
                else:
                    varsTable.append([len(functionDir), n, t, v, ''])
            else:
                print('The variable',n,'is not a',t)
        

        if t == 'float':
            if typeChecker.isFloat(v):
                if len(functionDir) == 1: 
                    global indexGlobalFloat
                    varsTable.append([len(functionDir), n, t, v, indexGlobalFloat])
                    indexGlobalFloat += 1
                else:
                    varsTable.append([len(functionDir), n, t, v, ''])
            else:
                print('The variable',n,'is not a',t)


        if t == 'String':
            if typeChecker.isString(v):
                if len(functionDir) == 1:
                    global indexGlobalString
                    varsTable.append([len(functionDir), n, t, v, indexGlobalString])
                    indexGlobalString += 1
                else:
                    varsTable.append([len(functionDir), n, t, v, ''])
            else:
                print('The variable',n,'is not a',t)
    else:
        print('The variable',n, 'is already defined') 
    

def pushTo_varsTable(n, t ): #Append it to the varTable when defining a var with NOT value
    
    if not checkIfVarIdExistsOnModule(n):
    
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


    else:
        print('The variable',n, 'is already defined')  
    



def reciveID(v):
    if checkIfVarIdExistsOnModule(v):
        print(v,'exist on module')
    else:
        if checkIfVarIdExistsOnGlobal(v):
            print(v,'exist on global')
        else:
            print(v, 'does not exist, you need to define it')

    
   
   



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
            


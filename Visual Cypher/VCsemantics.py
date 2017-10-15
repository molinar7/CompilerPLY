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
    

def pushTo_varsTable_WithCTE(n, t, c): #Append it to the varTable when defining a var with value
    if not checkIfVarIdExistsOnModule(n):

        if t == 'int':
            if typeChecker.isInt(c):
                if len(functionDir) == 1: # We know that is global if the index is 1
                    global indexGlobalInt
                    varsTable.append([len(functionDir), n, t, c, indexGlobalInt])
                    indexGlobalInt += 1
                else:
                    varsTable.append([len(functionDir), n, t, c])
            else:
                print('The variable',n,'is not a',t)
        

        if t == 'float':
            if typeChecker.isFloat(c):
                if len(functionDir) == 1: 
                    global indexGlobalFloat
                    varsTable.append([len(functionDir), n, t, c, indexGlobalFloat])
                    indexGlobalFloat += 1
                else:
                    varsTable.append([len(functionDir), n, t, c])
            else:
                print('The variable',n,'is not a',t)


        if t == 'String':
            if typeChecker.isString(c):
                if len(functionDir) == 1:
                    global indexGlobalString
                    varsTable.append([len(functionDir), n, t, c, indexGlobalString])
                    indexGlobalString += 1
                else:
                    varsTable.append([len(functionDir), n, t, c])
            else:
                print('The variable',n,'is not a',t)
    else:
        print('The variable',n, 'is already defined') 
    

def pushTo_varsTable(n, t ): #Append it to the varTable when defining a var with NOT value
    
    if not checkIfVarIdExistsOnModule(n):
    
        if t == 'int':
            global indexGlobalInt
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t, indexGlobalInt])
                indexGlobalInt +=1
            else:
                varsTable.append([len(functionDir), n, t])

        if t == 'float':
            global indexGlobalFloat
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t, indexGlobalFloat])
                indexGlobalFloat +=1
            else:
                varsTable.append([len(functionDir), n, t])

        if t == 'String':
            global indexGlobalString
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t, indexGlobalString])
                indexGlobalString +=1
            else:
                varsTable.append([len(functionDir), n, t])


    else:
        print('The variable',n, 'is already defined')  
    



def reciveID(v):
    print(len(functionDir))
    
   
   



def checkIfFunctionExists(n): # check that functions do not repeat
    for nombre in functionDir:
       if n == nombre[1]:
           return True    
    return False  

def checkIfVarIdExistsOnModule(n): # check if Var ID exists on module
   # print(len(functionDir))
   # print(n)
    for varID in varsTable:
        #print(n, varID)
        if len(functionDir) != varID[0]: # Unicamente queremos que busque en su modulo
            break
        else:
            if varID[1] == n:
                return True
            else:
                return False


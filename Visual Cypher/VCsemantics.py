functionDir = [[1,'global', None]]
varsTable = []

#len(functionDir) nos ayuda a saber en que scope nos ubicamos :)

def pushTo_FunctionDir(n,t):
    if not checkIfFunctionExists(n):
        functionDir.append([ len(functionDir) + 1, n, t])
    else:
        print('The function',n, 'is already defined')
    

def pushTo_varsTable_WithCTE(n, t, c): #append it to the table with value
    if not checkIfVarIdExists(n):
        varsTable.append([len(functionDir), n, t, c])
    else:
        print('The variable',n, 'is already defined') 
    

def pushTo_varsTable(n, t ): #append it to the table without a value
    if not checkIfVarIdExists(n):
        varsTable.append([len(functionDir), n, t])
    else:
        print('The variable',n, 'is already defined')  
    


def checkIfFunctionExists(n): # check that functions do not repeat
    for nombre in functionDir:
       if n == nombre[1]:
           return True    
    return False  

def checkIfVarIdExists(n): # check if Var ID exists on module
   # print(len(functionDir))
    for varID in varsTable:
        if len(functionDir) != varID[0]:
            break
        else:
            if varID[1] == n:
                return True
            else:
                return False

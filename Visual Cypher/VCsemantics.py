functionDir = [[1,'global', None]]
varTable = []

def pushTo_FunctionDir(n,t):
    if checkIfFunctionExists(n):
        functionDir.append([ len(functionDir) + 1, n, t])
    else:
        print('The function',n, 'is already defined')
    



def checkIfFunctionExists(n): # check that functions do not repeat
    for nombre in functionDir:
       if n == nombre[1]:
           return False     
    return True   



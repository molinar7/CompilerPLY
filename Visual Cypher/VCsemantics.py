import typeChecker
import VCquadruples
from VCmemory import *




#len(functionDir) nos ayuda a saber en que scope nos ubicamos :)

#['index','scopeName', 'returnType','counter to help when the function starts', 'numberOfParameters', 'Number of variables defined']
functionDir = [[1,'global', None]] # El directorio de funciones
varsTable = [] #LA tabla de variables
cteTable = [] # Tabla de constantes para no perder el valor
functionSignature = [] # Esta lista nos ayuda a saber de que tipo son los aprametros de cada funcion
arrDim = []




def validateSemanticCube(operator,left_op, right_op): # esta funcion comprueba las operaciones entre tipos
    #Example: cuboSemantico = [left_type, right_type, operator, typeResult]
    for element in typeChecker.cuboSemantico:
        if element[0] == left_op and element [1] == right_op and element [2] == operator:
            return element[3] # Regresamos el tipo de dato de la operacion resultante


def pushTo_FunctionDir(n,t, lineno):
    if not checkIfFunctionExists(n):
        
        getContextTypeQty()
        getTempsTypeQty()
        functionDir.append([ len(functionDir) + 1, n, t])
        resetScopeIndexs() # Resetea los indixes de la memoria ya que se cambio de contexto
    else:
        print('ERROR:', 'The function',n, 'at line:', lineno, 'is already defined')
        quit()




def pushTo_varsTable(n, t, lineno ): #Append it to the varTable when defining a var with NOT value

    if not checkIfVarIdExistsOnModule(n): # Checa que no exista en el modulo actual la variable

        if t == 'int':
            
            global indexGlobalInt, indexLocalInt
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t,  indexGlobalInt])
                indexGlobalInt +=1
                
            else:
                varsTable.append([len(functionDir), n, t, indexLocalInt])
                indexLocalInt += 1

        if t == 'float':
            global indexGlobalFloat, indexLocalFloat
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t, indexGlobalFloat])
                indexGlobalFloat +=1
            else:
                varsTable.append([len(functionDir), n, t, indexLocalFloat])
                indexLocalFloat += 1

        if t == 'String':
            global indexGlobalString, indexLocalString
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t,indexGlobalString])
                indexGlobalString +=1
            else:
                varsTable.append([len(functionDir), n, t, indexLocalString])
                indexLocalString += 1

        if t == 'boolean':
            global indexGlobalBoolean, indexLocalBoolean
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t, indexGlobalBoolean])
                indexGlobalBoolean +=1
            else:
                varsTable.append([len(functionDir), n, t, indexLocalBoolean])
                indexLocalBoolean += 1


    else:
        print('ERROR:', 'The variable',n,'at line',  lineno, 'is already defined')
        quit()


def push_cte_toTable(cte, lineno):
    #cteTable = [ cteValue, cteType, memIndex]
    global indexCtelInt, indexCteFloat, indexCteBoolean,  indexCteString

    for ctes in cteTable:# Sirve para no agregar constantes repetidas
        if ctes[0] == cte: 
            return ctes[0], ctes[1], ctes[2] # regresa la constante ya existente y no hace lo de abajo
  
    if typeChecker.isInt(cte):
        cteTable.append([ cte, 'int', indexCtelInt])
        indexCtelInt += 1
        return cte, 'int', indexCtelInt -1
    else:
        if typeChecker.isFloat(cte):
            cteTable.append([cte, 'float', indexCteFloat])
            indexCteFloat +=1
            return cte, 'float', indexCteFloat -1
        else:
            if typeChecker.isBoolean(cte):
                cteTable.append([ cte,'Boolean',  indexCteBoolean])
                indexCteBoolean +=1
                return cte,'boolean', indexCteBoolean -1 # menos 1 porque ya le sumamos uno arriba
            else:
                if typeChecker.isString(cte):
                    cteTable.append([ cte,'String',  indexCteString])
                    indexCteString +=1
                    return cte,'String', indexCteString -1 # menos 1 porque ya le sumamos uno arriba
                else:
                    print('ERROR: al line: ',lineno, ',', cte, 'is not a valid constant')
                    quit()

def createArrInfo(lim_inf, lim_sup):
    context = varsTable[-1][0] # con esto sabemos el contexto del arreglo
    arrId = varsTable[-1][1] # Con esto sabemos cual es la id del array, (es el ultimo agreado a varstable)
    arrMemIndex = varsTable[-1][3]
    arrType = varsTable[-1][2]# el tipo de arreglo

    #[context, id, type,  -k, lim_inf, lim_sup]
    arrDim.append([context, arrId, -(lim_inf), lim_inf, lim_sup])

    m0 =   lim_sup - lim_inf + 1 # la cantidad de casillas que ocupara el arreglo
   
    if arrType == 'int':
        global indexGlobalInt, indexLocalInt
        if context == 1:
            indexGlobalInt = indexGlobalInt + m0 -1 # este menos uno se quita porque mis indices empiezan en 01 y no en 00
        else:
            indexLocalInt = indexLocalInt + m0 -1

    if arrType == 'float':
        global indexGlobalFloat, indexLocalFloat
        if context == 1:
            indexGlobalFloat = indexGlobalFloat + m0 -1
        else:
            indexLocalFloat = indexLocalFloat + m0 -1

    if arrType == 'String':
        global indexGlobalString, indexLocalString
        if context == 1:
            indexGlobalString = indexGlobalString + m0 -1 
        else:
            indexLocalString = indexLocalString + m0 -1

    if arrType == 'boolean':
        global indexGlobalBoolean, indexLocalBoolean
        if context == 1:
            indexGlobalBoolean = indexGlobalBoolean + m0 -1
        else:
            indexLocalBoolean = indexLocalBoolean + m0 -1

    
    
    

def validateIDScope(v, lineno): # Esta funcion nos sirve para ver que scope tiene la id

    if checkIfVarIdExistsOnModule(v): # Se checa si existe primero en el modulo
        #print(v,'exist on module')
        for id in varsTable:
                if id[0] == len(functionDir): # si es igual a uno sabemos que es global
                    if id[1] == v:
                        return id[1], id[2], id[3] #  = varName, varType,  varMemIndex

    else:
        if checkIfVarIdExistsOnGlobal(v):# Se checa si existe despues en las variables globales
           # print(v,'exist on global')
            for id in varsTable:
                if id[0] == 1: # si es igual a uno sabemos que es global
                    if id[1] == v:
                        return id[1], id[2], id[3] #  = varName, varType, varMemIndex




        else:# Si no existe en en modulo ni en las variavles globales pues no esta definida
            print('ERROR:', v, 'at line', lineno ,'does not exist, you need to define it')
            quit()


def validateArrIdScope (id, lineno): #BORRAR maybeee no se usaaa pero s epodria usar
     if checkIfVarIdExistsOnModule(id):
         for element in arrDim:
             if element[0] == len(functionDir):
                 if element[1] == id:
                    return element[2],element[3],element[4]# k,lim_inf, lim_sup
     else:# Si el arreglo no existio en el contexto actual entonces debe ser global
        if checkIfVarIdExistsOnGlobal(id):
            for element in arrDim:
                if element[0] == 1:
                    if element[1] == id:
                        return element[2],element[3],element[4] #  k,lim_inf, lim_sup
        else:
            print('ERROR:', id, 'at line', lineno ,'does not exist, you need to define it')
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



def returnFunctionIndex(id):
    for element in functionDir:
        if element[1] == id:
            return element[0]

def returnFunctionParamNumbers(index):
    for element in functionDir:
        if element[0] == index:
            return element[4]

def getFunctionName(index):
    for element in functionDir:
        if element[0] == index:
            return element[1]

def getFunctionType(index):
    for element in functionDir:
        if element[0] == index:
            return element[2]
    
def getFunctionQuadrupleStart(index):
    for element in functionDir:
        if element[0] == index:
            return element[3]


# checa que los parametros de la llamada de funcion correspondan
# a la funcion
def validateFunctionParams(index, paramCounter, paramType, lineno):

    for element in functionDir:# Valida que no sean mas parametros en las llamadas!
        if element[0] == index and paramCounter > element[4]:
            print('TypeError: more positional arguments at line ',  lineno)
            quit() 

    for element in functionSignature:
        if element[0] == index:
            if element[paramCounter][0] == paramType:
                return True
            else:
                return False

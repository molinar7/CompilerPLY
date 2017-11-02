import VCsemantics
import VCparser

globalVarTypeQty = []
localVarTypeQty = [] # Esta lista nos sirve para saber cuantas variables de cada tipo hay en locales
cteTypeQty = []
tempTypeQty = []

#Variables globales
indexGlobalInt = 100001 
indexGlobalFloat = 130001
indexGlobalString = 160001
indexGlobalBoolean = 180001

#Variables locales
indexLocalInt = 20001
indexLocalFloat = 23001
indexLocalString = 26001
indexLocalBoolean = 28001

#Variables temporales
indexTemporalInt = 30001
indexTemporalFloat = 33001
indexTemporalString = 36001
indexTemporalBoolean = 38001

#Constantes
indexCtelInt = 40001
indexCteFloat = 43001
indexCteString = 46001
indexCteBoolean = 48001


def resetScopeIndexs():
    VCsemantics.indexLocalInt = 20001
    VCsemantics.indexLocalFloat = 23001
    VCsemantics.indexLocalString = 26001
    VCsemantics.indexLocalBoolean = 28001  

    # Hacemos esto porque estas variables globales solamente se usan en esta clase
    global indexTemporalInt, indexTemporalFloat, indexTemporalString, indexTemporalBoolean
    indexTemporalInt = 30001
    indexTemporalFloat = 33001
    indexTemporalString = 36001
    indexTemporalBoolean = 38001



def getTempIndex (typeResult):
    global indexTemporalInt, indexTemporalFloat, indexTemporalString, indexTemporalBoolean
    if typeResult =='int':
        indexTemporalInt +=1
        return indexTemporalInt -1
    if typeResult == 'float':
        indexTemporalFloat +=1
        return indexTemporalFloat -1
    if typeResult == 'String':
        indexTemporalString +=1
        return indexTemporalString -1
    if typeResult == 'boolean':
        indexTemporalBoolean +=1
        return indexTemporalBoolean -1
        

def getContextTypesQty(): # Sirve para no desperdiciar memoria al saber los la cantidad de tipos
    numberInts = 0 
    numberFloat = 0
    numberString = 0
    numberBoolean = 0
    for context in VCsemantics.functionDir:
        for variable in VCsemantics.varsTable:
            if context[0] == variable[0]: # para nomas contar los tipos en el mismo contexto

                if variable[2] == 'int':
                    numberInts += 1
                if variable[2] == 'float':
                    numberFloat += 1
                if variable[2] == 'String':
                    numberString += 1
                if variable[2] == 'boolean':
                    numberBoolean += 1
        if context[0] == 1:
            globalVarTypeQty.append([context[1], numberInts, numberFloat, numberString, numberBoolean])
        else:
            localVarTypeQty.append([context[1], numberInts, numberFloat, numberString, numberBoolean])
        numberInts = 0 # se resetean en cada cambio de contexto
        numberFloat = 0
        numberString = 0
        numberBoolean = 0
    
        


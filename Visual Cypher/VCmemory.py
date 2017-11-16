import VCsemantics
import VCparser

globalVarTypeQty = ['global']
localVarTypeQty = ['local'] # Esta lista nos sirve para saber cuantas variables de cada tipo hay en locales
cteTypeQty = ['cte']
tempTypeQty = ['temps']

#Variables globales
indexGlobalInt = 10001 
indexGlobalFloat = 13001
indexGlobalString = 16001
indexGlobalBoolean = 18001

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
        

       
def getContextTypeQty():
    contextName = VCsemantics.functionDir[-1][1]
    context = VCsemantics.functionDir[-1][0]
 
    
    if context == 1:
        globalVarTypeQty.append([ VCsemantics.indexGlobalInt - 10001, VCsemantics.indexGlobalFloat - 13001, 
                                VCsemantics.indexGlobalString - 16001, VCsemantics.indexGlobalBoolean - 18001])

    else:
        localVarTypeQty.append([context, VCsemantics.indexLocalInt - 20001, VCsemantics.indexLocalFloat - 23001, 
                            VCsemantics.indexLocalString - 26001, VCsemantics.indexLocalBoolean - 28001])

def getTempsTypeQty():
    context = VCsemantics.functionDir[-1][0]
    contextName = VCsemantics.functionDir[-1][1]
  
    
    # insertamos a la lista el conteo de las variables temporales
    tempTypeQty.append([context, indexTemporalInt - 30001, 
                        indexTemporalFloat - 33001, indexTemporalString - 36001, indexTemporalBoolean - 38001])



import VCsemantics
import VCparser

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

    VCsemantics.indexCtelInt = 40001
    VCsemantics.indexCteFloat = 43001
    VCsemantics.indexCteString = 46001
    VCsemantics.indexCteBoolean = 48001

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
        
from VCquadruples import *
from vcvirtualMemoryHandler import *
import VCmemory

globalMemory = []
localMemory = []
tempMemory = []
cteMemory = []

def execution():

    #Creaciond de las memorias
    createGlobalMemory()
    createLocalMemory(VCmemory.localVarTypeQty[-1][0]) # Siempre la primer memoria local que se crea es la global
    createTempMemory(VCmemory.tempTypeQty[-1][0])

    

    quadrupleTravel()
    print(globalMemory)
    print(localMemory)
    print(tempMemory)
   
   
  
def createGlobalMemory():
    intQty = VCmemory.globalVarTypeQty[1][0] # La cantidad de enteros que tendra la memoria global
    floatQty = VCmemory.globalVarTypeQty[1][1] # la cantidad de flotantes que tendra la memoria global
    stringQty = VCmemory.globalVarTypeQty[1][2]
    booleanQty = VCmemory.globalVarTypeQty[1][3]

    intList = [None] * intQty 
    globalMemory.append(intList)

    floatList = [None] * floatQty
    globalMemory.append(floatList)

    stringList = [None] * stringQty
    globalMemory.append(stringList)

    booleanList = [None] * booleanQty
    globalMemory.append(booleanList)

def createLocalMemory(contextIndex):
    for context in VCmemory.localVarTypeQty: # se busca el contexto local en el que se desea crear la memoria
        if context[0] == contextIndex:
            intQty = context[1]
            floatQty = context[2]
            stringQty = context[3]
            booleanQty = context[4]
            break

    intList = [None] * intQty 
    localMemory.append(intList)

    floatList = [None] * floatQty
    localMemory.append(floatList)

    stringList = [None] * stringQty
    localMemory.append(stringList)

    booleanList = [None] * booleanQty
    localMemory.append(booleanList)

def createTempMemory(contextIndex):
    for context in VCmemory.tempTypeQty: # se busca el contexto local en el que se desea crear la memoria
        if context[0] == contextIndex:
            intQty = context[1]
            floatQty = context[2]
            stringQty = context[3]
            booleanQty = context[4]
            break

    intList = [None] * intQty 
    tempMemory.append(intList)

    floatList = [None] * floatQty
    tempMemory.append(floatList)

    stringList = [None] * stringQty
    tempMemory.append(stringList)

    booleanList = [None] * booleanQty
    tempMemory.append(booleanList)
           


 


def quadrupleTravel():
    pointer = 0

    while quadruples[pointer][0] != 'END':
       


        if quadruples[pointer][0] == 'goto':
            pointer = quadruples[pointer][3] # cuando hay asignacion siempre poner un continue para que no se incremente el pointer
            continue 

        elif quadruples[pointer][0] == '=':
           result = getFromMemory(quadruples[pointer][1]) # guarda el valor del mem index de la izq
           setToMemory(quadruples[pointer][3], result)# se envia el memIndex y el valor que se guardara en ese mem index

        
        elif quadruples[pointer][0] == '+':
             left_value = getFromMemory(quadruples[pointer][1]) # guarda el valor del mem index de la izq
             right_value = getFromMemory(quadruples[pointer][2])
             result = left_value + right_value
             setToMemory(quadruples[pointer][3], result)

        elif quadruples[pointer][0] == '-':
             left_value = getFromMemory(quadruples[pointer][1]) # guarda el valor del mem index de la izq
             right_value = getFromMemory(quadruples[pointer][2])
             result = left_value - right_value
             setToMemory(quadruples[pointer][3], result)

        elif quadruples[pointer][0] == '*':
             left_value = getFromMemory(quadruples[pointer][1]) # guarda el valor del mem index de la izq
             right_value = getFromMemory(quadruples[pointer][2])
             result = left_value * right_value
             setToMemory(quadruples[pointer][3], result)

        elif quadruples[pointer][0] == '/':
             left_value = getFromMemory(quadruples[pointer][1]) # guarda el valor del mem index de la izq
             right_value = getFromMemory(quadruples[pointer][2])
             result = left_value / right_value
             setToMemory(quadruples[pointer][3], result)
        
        pointer += 1
            
            
   





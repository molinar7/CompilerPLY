from VCquadruples import *
from vcvirtualMemoryHandler import *
import VCmemory
import VCgui


localMemoryStack = [] # donde se duermen y despierta los contextos
tempMemoryStack = []

jumpPointer = [] # Pila para saber a que quadruplo regrear cuando se acabe una funcion

globalMemory = []
localMemory = []
tempMemory = []
cteMemory = []

nextFunctionIndex = [] # para saber cual es el indice de la siguiente funcion cuando se encuentra 'era'
nextParamIndex = [] # indice donde se guardara el old param
oldParamIndex = [] 

returnStack = []


def execution():

    #Creaciond de las memorias
    createGlobalMemory()
    createLocalMemory(VCmemory.localVarTypeQty[-1][0]) #  0 porque siempre la primer memoria local que se crea es la main
    createTempMemory(VCmemory.tempTypeQty[-1][0])

    

    quadrupleTravel()
 
   
   
  
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
    global localMemory, tempMemory, localMemoryStack, tempMemoryStack
    pointer = 0

    while quadruples[pointer][0] != 'END':
        #print('Pointer at: ',  pointer)
    
       


        if quadruples[pointer][0] == 'goto':
            pointer = quadruples[pointer][3] # cuando hay asignacion siempre poner un continue para que no se incremente el pointer con el ciclo
            continue 

        elif quadruples[pointer][0] == '=':

          if not isinstance(quadruples[pointer][1], int): # diferencia un memindex a una casilla de array (memindex)
                result = getFromMemory(getFromMemory(int(quadruples[pointer][1][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
          else:
                result = getFromMemory(quadruples[pointer][1])

          if result == None:
                    print('Variable not initialized')
                    quit()
                

          if not isinstance(quadruples[pointer][3], int):
                storage = getFromMemory(int(quadruples[pointer][3][1:-1])) # Le quitamos los parentesis y se convierte a string
                
                setToMemory(storage, result) # a la casilla direccionada se le pone el result ( por eso se le pone entre parentesis)
          else:
                setToMemory(quadruples[pointer][3], result) 


        elif quadruples[pointer][0] == '+':
            if not isinstance(quadruples[pointer][1], int):
                left_value = getFromMemory(getFromMemory(int(quadruples[pointer][1][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
            else:
                left_value = getFromMemory(quadruples[pointer][1])
            if not isinstance(quadruples[pointer][2], int):
                right_value = getFromMemory(getFromMemory(int(quadruples[pointer][2][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
            else:
                right_value = getFromMemory(quadruples[pointer][2])  

            
            if left_value == None or right_value == None:
               print('Variable not initialized')
               quit()
            result = left_value + right_value
            setToMemory(quadruples[pointer][3], result)

        elif quadruples[pointer][0] == '-':
              if not isinstance(quadruples[pointer][1], int):
                left_value = getFromMemory(getFromMemory(int(quadruples[pointer][1][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
              else:
                left_value = getFromMemory(quadruples[pointer][1])
              if not isinstance(quadruples[pointer][2], int):
                right_value = getFromMemory(getFromMemory(int(quadruples[pointer][2][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
              else:
                right_value = getFromMemory(quadruples[pointer][2]) 

              if left_value == None or right_value == None:
                print('Variable not initialized')
                quit()
              result = left_value - right_value
              setToMemory(quadruples[pointer][3], result)

        elif quadruples[pointer][0] == '*':
             if not isinstance(quadruples[pointer][1], int):
                left_value = getFromMemory(getFromMemory(int(quadruples[pointer][1][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
             else:
                left_value = getFromMemory(quadruples[pointer][1])
             if not isinstance(quadruples[pointer][2], int):
                right_value = getFromMemory(getFromMemory(int(quadruples[pointer][2][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
             else:
                right_value = getFromMemory(quadruples[pointer][2])

             if left_value == None or right_value == None:
               print('Variable not initialized')
               quit()
             result = left_value * right_value
             setToMemory(quadruples[pointer][3], result)

        elif quadruples[pointer][0] == '/':
             if not isinstance(quadruples[pointer][1], int):
                left_value = getFromMemory(getFromMemory(int(quadruples[pointer][1][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
             else:
                left_value = getFromMemory(quadruples[pointer][1])
             if not isinstance(quadruples[pointer][2], int):
                right_value = getFromMemory(getFromMemory(int(quadruples[pointer][2][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
             else:
                right_value = getFromMemory(quadruples[pointer][2])
             if left_value == None or right_value == None:
               print('Variable not initialized')
               quit()
             result = left_value / right_value
             setToMemory(quadruples[pointer][3], result)
        

        elif quadruples[pointer][0] == 'print':
             left_value = quadruples[pointer][1] 
             
             if not isinstance(left_value, int): # Cuando no es int entonces es un string osea tiene parentesis
                left_value = int(left_value[1:-1]) # Le quitamos los parentesis y se convierte a string
                casilla = getFromMemory(getFromMemory(left_value))
                VCgui.pantalla.insert('end-1c',  '\n')
                VCgui.pantalla.insert('end-1c', casilla )
                print(casilla)
              
             else:
                casilla = getFromMemory(left_value)
                VCgui.pantalla.insert('end-1c',  '\n')
                VCgui.pantalla.insert('end-1c', casilla )
                print(casilla)

        
        elif quadruples[pointer][0] == '>':
             if not isinstance(quadruples[pointer][1], int):
                left_value = getFromMemory(getFromMemory(int(quadruples[pointer][1][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
             else:
                left_value = getFromMemory(quadruples[pointer][1])
             if not isinstance(quadruples[pointer][2], int):
                right_value = getFromMemory(getFromMemory(int(quadruples[pointer][2][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
             else:
                right_value = getFromMemory(quadruples[pointer][2])

             if left_value == None or right_value == None:# previene var no inlicialisadas
               print('Variable not initialized')
               quit()
            
             if left_value > right_value:
               result = True
             else:
               result = False

             setToMemory(quadruples[pointer][3], result)
        
        elif quadruples[pointer][0] == '<':

             if not isinstance(quadruples[pointer][1], int):
                left_value = getFromMemory(getFromMemory(int(quadruples[pointer][1][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
             else:
                left_value = getFromMemory(quadruples[pointer][1])
             if not isinstance(quadruples[pointer][2], int):
                right_value = getFromMemory(getFromMemory(int(quadruples[pointer][2][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
             else:
                right_value = getFromMemory(quadruples[pointer][2])

             
            
             if left_value < right_value:
               result = True
             else:
               result = False

             setToMemory(quadruples[pointer][3], result)

        elif quadruples[pointer][0] == '==':
             if not isinstance(quadruples[pointer][1], int):
                left_value = getFromMemory(getFromMemory(int(quadruples[pointer][1][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
             else:
                left_value = getFromMemory(quadruples[pointer][1])
             if not isinstance(quadruples[pointer][2], int):
                right_value = getFromMemory(getFromMemory(int(quadruples[pointer][2][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
             else:
                right_value = getFromMemory(quadruples[pointer][2])

             
            
             if left_value == right_value:
               result = True
             else:
               result = False

             setToMemory(quadruples[pointer][3], result)

        elif quadruples[pointer][0] == '<=':
             left_value = getFromMemory(quadruples[pointer][1]) # guarda el valor del mem index de la izq
             right_value = getFromMemory(quadruples[pointer][2])

             
            
             if left_value <= right_value:
               result = True
             else:
               result = False

             setToMemory(quadruples[pointer][3], result)

        elif quadruples[pointer][0] == '>=':
             left_value = getFromMemory(quadruples[pointer][1]) # guarda el valor del mem index de la izq
             right_value = getFromMemory(quadruples[pointer][2])

             
            
             if left_value >= right_value:
               result = True
             else:
               result = False

             setToMemory(quadruples[pointer][3], result)

        elif quadruples[pointer][0] == '!=':
             left_value = getFromMemory(quadruples[pointer][1]) # guarda el valor del mem index de la izq
             right_value = getFromMemory(quadruples[pointer][2])

             
            
             if left_value != right_value:
               result = True
             else:
               result = False

             setToMemory(quadruples[pointer][3], result)
        
        elif quadruples[pointer][0] == 'and':
             left_value = getFromMemory(quadruples[pointer][1]) # guarda el valor del mem index de la izq
             right_value = getFromMemory(quadruples[pointer][2])

             
            
             if left_value == True and right_value == True:
               result = True
             else:
               result = False

             setToMemory(quadruples[pointer][3], result)
        
        elif quadruples[pointer][0] == 'or':
             left_value = getFromMemory(quadruples[pointer][1]) # guarda el valor del mem index de la izq
             right_value = getFromMemory(quadruples[pointer][2])

             
            
             if left_value == True or right_value == True:
               result = True
             else:
               result = False

             setToMemory(quadruples[pointer][3], result)

             
        elif quadruples[pointer][0] == 'gotoF':
             left_value = getFromMemory(quadruples[pointer][1]) # guarda el valor del mem index de la izq
             if left_value == False:
                 pointer = quadruples[pointer][3]
                 continue

        elif quadruples[pointer][0] == 'ver': # Verifica el index del array
          arrIndex = getFromMemory(quadruples[pointer][1])
          lim_inf = quadruples[pointer][2] # no hace falta llamar a get porque el valor ya esta en el quadruplo
          lim_sup = quadruples[pointer][3]
          if arrIndex < lim_inf or arrIndex > lim_sup:
            print('ERROR: Array index out of bonds')
            quit()

        elif quadruples[pointer][0] == '+-k':
             left_value = getFromMemory(quadruples[pointer][1]) # guarda el valor del mem index de la izq
             right_value = quadruples[pointer][2] # sin el get porque el valor de k esta en el cuadruplo

             if left_value == None or right_value == None:
               print('Variable not initialized')
               quit()
             result = left_value + right_value
             setToMemory(quadruples[pointer][3], result)

        elif quadruples[pointer][0] == '+base':
             left_value = getFromMemory(quadruples[pointer][1]) # guarda el valor del mem index de la izq
             right_value = quadruples[pointer][2] # sin el get porque el valor de la base ya esta en el cuadruplo

             if left_value == None or right_value == None:
               print('Variable not initialized')
               quit()
             result = left_value + right_value
             setToMemory(quadruples[pointer][3], result)

        elif quadruples[pointer][0] == 'era': # Cuadruplo para crear memorias
          
          nextFunctionIndex.append(quadruples[pointer][3]) # para saber cual es el indice a la funcion a llamar
    
        elif quadruples[pointer][0] == 'param':

          param = quadruples[pointer][3]
          param = int(param[-1:])

          for signature in VCsemantics.functionSignature:
            if signature[0] == quadruples[pointer][2]:
              paramIndex = signature[param][1]
              nextParamIndex.append(paramIndex)

          # se tiene que guardar el parametro ya que se dormira la memoria para despues asignarlo a su parametro del nuevo contexto
          if not isinstance(quadruples[pointer][1], int):
                oldParamIndex.append(getFromMemory(getFromMemory(int(quadruples[pointer][1][1:-1])))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
          else:
                oldParamIndex.append(getFromMemory(quadruples[pointer][1])) 
     

        elif quadruples[pointer][0] == 'gosub': 

          localMemoryStack.append(localMemory) # se duerme la memoria
          tempMemoryStack.append(tempMemory) # se duerme la memoria
          
          localMemory =[] # despues de dormirla deja de estar activa
          tempMemory = []

          nIndex = nextFunctionIndex.pop()
          createLocalMemory(nIndex) # se crea la nueva memoria
          createTempMemory(nIndex)

          for i in range (0 , len(nextParamIndex)): # em este for esta toda la logica para guardar parametros en nuevas funciones
            setToMemory(nextParamIndex.pop(), oldParamIndex.pop())

          jumpPointer.append(pointer) # para saber a donde regresar cuando te encuentres un return o end proc
          pointer = quadruples[pointer][3]
          continue

        elif quadruples[pointer][0] == 'ENDPROC': 
          
          pointer = jumpPointer.pop() + 1
          localMemory = localMemoryStack.pop() # a despertar chiquitas!
          tempMemory = tempMemoryStack.pop()
          continue
          
          
          
        elif quadruples[pointer][0] == 'return':
          if not isinstance(quadruples[pointer][1], int): # diferencia un memindex a una casilla de array (memindex)
                left_op = getFromMemory(getFromMemory(int(quadruples[pointer][1][1:-1]))) # primero convertimos a int luego obtenemos el memindex del valor del array y luego el valor del memIndex
          else:
                left_op = getFromMemory(quadruples[pointer][1]) 
          
          returnStack.append(left_op)

          pointer = jumpPointer.pop() + 1
          localMemory = localMemoryStack.pop() # a despertar chiquitas!
          tempMemory = tempMemoryStack.pop()
          continue
          
        elif quadruples[pointer][0] == '=r':
          result = returnStack.pop()
          setToMemory(quadruples[pointer][3], result)


        pointer += 1
            

   





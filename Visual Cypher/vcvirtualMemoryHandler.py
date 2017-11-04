import VCsemantics
import VCvirtualMemory

def getCteValue(memIndex): # recibe un mem index de una cte y nos regresa su valor 
    for cte in VCsemantics.cteTable:
        if cte[2] ==  memIndex:
            return cte[0]



def getFromMemory(memIndex):
#-------------Global-------------
    if memIndex >= 10001 and memIndex<= 13000:
        return VCvirtualMemory.globalMemory[0][memIndex - 10001]
    elif  memIndex >= 13001 and memIndex<= 16000: 
        return VCvirtualMemory.globalMemory[1][memIndex - 13001]
    elif  memIndex >= 16001 and memIndex<= 18000: 
        return VCvirtualMemory.globalMemory[2][memIndex - 16001]
    elif  memIndex >= 18001 and memIndex<= 20000: 
        return VCvirtualMemory.globalMemory[3][memIndex - 18001]

#----------------Local----------------------------------
    elif memIndex >= 20001 and memIndex<= 23000:
        return VCvirtualMemory.localMemory[0][memIndex - 20001]
    elif  memIndex >= 23001 and memIndex<= 26000: 
        return VCvirtualMemory.localMemory[1][memIndex - 23001]
    elif  memIndex >= 26001 and memIndex<= 28000: 
        return VCvirtualMemory.localMemory[2][memIndex - 26001] 
    elif  memIndex >= 28001 and memIndex<= 30000: 
        return VCvirtualMemory.localMemory[3][memIndex - 28001]

#----------------Temporal----------------------------------
    elif memIndex >= 30001 and memIndex<= 33000:
        return VCvirtualMemory.tempMemory[0][memIndex - 30001]
    elif  memIndex >= 33001 and memIndex<= 36000: 
        return VCvirtualMemory.tempMemory[1][memIndex - 33001]
    elif  memIndex >= 36001 and memIndex<= 38000: 
        return VCvirtualMemory.tempMemory[2][memIndex - 36001] 
    elif  memIndex >= 38001 and memIndex<= 40000: 
        return VCvirtualMemory.tempMemory[3][memIndex - 38001]


#----------------CTE----------------------------------
    elif memIndex >= 40001 and memIndex<= 50000:
        return getCteValue(memIndex)
    


def setToMemory(memIndex, value):
#-------------Global-------------
    if memIndex >= 10001 and memIndex<= 13000:
        VCvirtualMemory.globalMemory[0][memIndex - 10001] = value

    elif  memIndex >= 13001 and memIndex<= 16000: 
        VCvirtualMemory.globalMemory[1][memIndex - 13001] = value

    elif  memIndex >= 16001 and memIndex<= 18000: 
        VCvirtualMemory.globalMemory[2][memIndex - 16001] = value

    elif  memIndex >= 18001 and memIndex<= 20000:
        VCvirtualMemory.globalMemory[3][memIndex - 18001] = value

#----------------Local----------------------------------
    elif memIndex >= 20001 and memIndex<= 23000:
        VCvirtualMemory.localMemory[0][memIndex - 20001] = value
    elif  memIndex >= 23001 and memIndex<= 26000: 
        VCvirtualMemory.localMemory[1][memIndex - 23001] = value
    elif  memIndex >= 26001 and memIndex<= 28000: 
        VCvirtualMemory.localMemory[2][memIndex - 26001] = value 
    elif  memIndex >= 28001 and memIndex<= 30000: 
        VCvirtualMemory.localMemory[3][memIndex - 28001] = value

#----------------Temporal----------------------------------
    elif memIndex >= 30001 and memIndex<= 33000:
        VCvirtualMemory.tempMemory[0][memIndex - 30001] = value
    elif  memIndex >= 33001 and memIndex<= 36000: 
        VCvirtualMemory.tempMemory[1][memIndex - 33001] = value
    elif  memIndex >= 36001 and memIndex<= 38000: 
        VCvirtualMemory.tempMemory[2][memIndex - 36001] = value
    elif  memIndex >= 38001 and memIndex<= 40000: 
        VCvirtualMemory.tempMemory[3][memIndex - 38001] = value

# No hay seccion de cte porque jamas se guarda un valor en una cte
  
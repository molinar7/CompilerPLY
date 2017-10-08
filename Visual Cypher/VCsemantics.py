procedureDir = ['global']

def addToProcedureDir(n):
        procedureDir.append(n)
   
    

def checkIfProcedureExists(x):
    for i in range (0,len(procedureDir)):
        if procedureDir[i] == x:
            return True
        else:
            return False
   



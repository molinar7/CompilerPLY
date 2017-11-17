from  tkinter import *
import VCparser
import VCvirtualMemory 
import VCsemantics


def compiler():
    VCparser.compiler()

def execution():
    VCvirtualMemory.execution() # ARRANCA LA EJECUCION!!!



            
    


mGui = Tk()


mGui.geometry('1000x650')
mGui.title('Visual Cypher')


textArea = Text(mGui, height=30, width=130)
textArea.pack()

frame = Frame(mGui, relief=RAISED, borderwidth=1)
frame.pack(fill=BOTH, expand=True)

pantalla = Text(mGui, height=10, width=130)
pantalla.pack()


frame = Frame(mGui, relief=RAISED, borderwidth=1)
frame.pack(fill=BOTH, expand=True)

executeButtom = Button(mGui, text = 'Execute', command = execution)
executeButtom.pack(side = RIGHT)

compileButtom= Button(mGui, text = 'Compile', command = compiler)
compileButtom.pack(side =RIGHT)


#reset_button = Button(mGui, text="Reset Environment", command=reset)
#reset_button.pack(side = LEFT)
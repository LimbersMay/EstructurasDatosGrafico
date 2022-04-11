from tkinter import *
from frontend.pila_interfaz import PilaInterfaz

class PilaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
    
        master.title("Estructura de datos Pila")

        # Elementos del frame
        self.label_titulo = Label(self, text="Pila")

        self.pila_interfaz = PilaInterfaz(self)

        # Posicionamiento de los elementos
        self.label_titulo.grid(row=0, column=0)
        self.pila_interfaz.grid(row=1, column=0)
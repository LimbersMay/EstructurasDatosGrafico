from tkinter import *
from estructuras_opciones.botones_template import BotonesBasicos
from frontend.pila_interfaz import PilaInterfaz

class PilaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
    
        master.title("Estructura de datos Pila")

        # Elementos del frame
        self.label_titulo = Label(self, text="Pila")
        self.pila_interfaz = PilaInterfaz(self)
        self.botones_inferiores = BotonesPila(self, self.pila_interfaz)

        # Posicionamiento de los elementos
        self.label_titulo.grid(row=0, column=0)
        self.pila_interfaz.grid(row=1, column=0)
        self.botones_inferiores.grid(row=2, column=0)


class BotonesPila(BotonesBasicos):
    def __init__(self, master, pila_interfaz):
        super().__init__(master, pila_interfaz)
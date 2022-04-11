from tkinter import *
from estructuras.pila.pila import Pila

class PilaInterfaz(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.pila = Pila()

        # Configuraciones de la ventana
        self.config(
            width = 400,
            height = 300,
            bg = 'brown',
        )

        self.grid_propagate(False)

        # Elementos de la ventana
        self.canvas = Canvas(self, width=200, height=150, bg='darkred')



        # Configuraciones de los elementos de la ventana



        # Posicionamiento de los elementos
        self.canvas.grid(row=1, column=0)

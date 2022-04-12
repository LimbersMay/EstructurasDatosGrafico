from tkinter import *
from frontend.lista_interfaz import ListaInterfaz

class ListaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de datos Lista")

        # Elementos del frame
        self.titulo = Label(self, text="Lista simplemente enlazada")
        self.lista_interfaz = ListaInterfaz(self)
        self.botones_inferiores = BotonesInferiores(self, self.lista_interfaz)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_interfaz.grid(row=1, column=0)
        self.botones_inferiores.grid(row=2, column=0)

class BotonesInferiores(Frame):
    def __init__(self, master, lista_interfaz):
        Frame.__init__(self, master)
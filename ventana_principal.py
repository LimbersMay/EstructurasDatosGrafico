from tkinter import *
from principal.titulo import Titulo
from principal.botones import Botones

class Ventana(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)

        # El usuario tendrá 7 opciones a elegir correspondientes a las 7 estructuras 
        master.title("Estructuras de Datos")
        master.geometry("400x500")

        # Elementos de la ventana principal

        # Textos de la ventana principal
        self.titulo = Titulo(self)
        self.botones = Botones(self)

        # Botones de la ventana principal

        # Posicionamiento de los elementos de la ventana principal
        self.titulo.grid(row=0, column=1)
        self.botones.grid(row=1, column=1)
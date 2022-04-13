from tkinter import *
from estructuras.cola import Cola
# Estructura básica dirigida para las colas y las pilas, pues ambos comparten métodos similares como lo son: insertar, eliminar y buscar.

class EstructuraSimple(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.estructura = Cola()
        self.lista_frames = []

        # Configuraciones de la ventana
        self.config(width=1000, height=350, bg="#146356")
        self.grid_propagate(False)

        self.rowconfigure(0, weight=1)
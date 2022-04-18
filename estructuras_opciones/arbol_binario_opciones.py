from tkinter import *
from estructuras.binary_tree import BinaryTree
from .templates.arbol_template import ArbolInterfaz

class ArbolBinarioOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.titulo = Label(self, text="Arbol Binario")
        self.arbol_interfaz = ArbolBinarioInterfaz(self)

        self.titulo.grid(row=0, column=0)
        self.arbol_interfaz.grid(row=1, column=0)

class ArbolBinarioInterfaz(ArbolInterfaz):
    def __init__(self, master):
        super().__init__(master)

        self.arbol = BinaryTree(5)

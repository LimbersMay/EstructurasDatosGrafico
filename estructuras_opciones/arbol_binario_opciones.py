from tkinter import *
from estructuras.binary_tree import BinaryTree
from .templates.arbol_template import ArbolInterfaz
from .templates.botones_arbol_template import BotonesArbol

class ArbolBinarioOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Arbol binario")

        self.titulo = Label(self, text="Arbol Binario simple")
        self.arbol_interfaz = ArbolBinarioInterfaz(self)
        self.botones = BotonesArbolBinario(self, self.arbol_interfaz)

        self.titulo.grid(row=0, column=0)
        self.arbol_interfaz.grid(row=1, column=0)
        self.botones.grid(row=2, column=0)

class ArbolBinarioInterfaz(ArbolInterfaz):
    def __init__(self, master):
        super().__init__(master)

        self.arbol = BinaryTree()
    
    def insertar_izquierda(self, elemento, referencia):
        self.arbol.insert_left(elemento, referencia)
        self.dibujar_arbol()

    def insertar_derecha(self, elemento, referencia):
        self.arbol.insert_right(elemento, referencia)
        self.dibujar_arbol()


class BotonesArbolBinario(BotonesArbol):
    def __init__(self, master, arbol_interfaz):
        super().__init__(master, arbol_interfaz)

        self.insertar_derecha = Button(self, text="Insertar Derecha", command=self.insertar_derecha)
        self.insertar_izquierda = Button(self, text="Insertar Izquierda", command=self.insertar_izquierda)

        self.referencia_label = Label(self, text="Referencia: ")
        self.referencia_entry = Entry(self)

        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.referencia_label.grid(row=0, column=2)
        self.referencia_entry.grid(row=0, column=3)

        self.insertar_raiz.grid(row=0, column=4)

        self.insertar_derecha.grid(row=0, column=5)
        self.insertar_izquierda.grid(row=0, column=6)

        self.eliminar.grid(row=0, column=7)
        self.buscar.grid(row=0, column=8)

    def insertar_izquierda(self):
        self.arbol_interfaz.insertar_izquierda(self.dato_entry.get(), self.referencia_entry.get())

    def insertar_derecha(self):
        self.arbol_interfaz.insertar_derecha(self.dato_entry.get(), self.referencia_entry.get())
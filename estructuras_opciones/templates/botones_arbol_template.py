from tkinter import *


class BotonesArbol(Frame):
    def __init__(self, master, arbol_interfaz):
        Frame.__init__(self, master)

        self.arbol_interfaz = arbol_interfaz

        # Elementos del frame
        self.dato_label = Label(self, text="Valor: ")
        self.dato_entry = Entry(self)

        self.eliminar = Button(self, text="Eliminar", command=self.eliminar)
        self.buscar = Button(self, text="Buscar", command=self.buscar)

        self.insertar_raiz = Button(self, text="Insertar raiz", command=self.insertar_raiz)
    
    def eliminar(self):
        self.arbol_interfaz.eliminar(self.dato_entry.get())
    
    def buscar(self):
        self.arbol_interfaz.buscar(self.dato_entry.get())

    def insertar_raiz(self):
        self.arbol_interfaz.insertar_raiz(self.dato_entry.get())
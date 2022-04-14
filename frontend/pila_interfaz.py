from tkinter import *
from estructuras.pila import Pila
from frontend.lista_simple_template import ListaInterfaz

class PilaInterfaz(ListaInterfaz):

    def __init__(self, master):
        super().__init__(master)

        self.lista = Pila()
    
    def insertar(self, valor):
        self.lista.insertar(valor)

        self.dibujar_lista()

    def eliminar(self):
        self.lista.eliminar()

        self.dibujar_lista()
    
    def buscar(self, valor):
        self.dibujar_lista(valor)
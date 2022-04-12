from tkinter import *
from estructuras.lista_enlazada.linked_list import LinkedList

class ListaInterfaz(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lista = LinkedList()

        # Configuraciones de la ventana
        self.config(width=300, height=300)
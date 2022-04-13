from tkinter import *
from estructuras.lista_enlazada.linked_list import LinkedList
from frontend.lista_interfaz import ListaInterfaz

class ListaSimpleInterfaz(ListaInterfaz):
    def __init__(self, master):
        super().__init__(master)
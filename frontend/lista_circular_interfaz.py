from tkinter import *
from estructuras.lista_circular.circular_list import CircularList
from frontend.lista_interfaz import ListaInterfaz

class ListaCircularInterfaz(ListaInterfaz):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lista = CircularList()
    
    # Métodos de la lista circular
    def rotar_izquierda(self):
        pass

    def rotar_derecha(self):
        pass
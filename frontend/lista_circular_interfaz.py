from tkinter import *
from estructuras.lista_circular.circular_list import CircularList
from frontend.lista_interfaz import ListaInterfaz

class ListaCircularInterfaz(ListaInterfaz):

    def __init__(self, master):
        super().__init__(master)

        self.lista = CircularList()
    
    # Métodos de la lista circular
    def rotar_izquierda(self):
        self.lista.move_left()

        self.dibujar_lista()

    def rotar_derecha(self):
        self.lista.move_right()

        self.dibujar_lista()
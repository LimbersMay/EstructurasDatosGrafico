from tkinter import *
from estructuras_opciones.botones_inf_listas import PlantillaBotones
from frontend.lista_circular_interfaz import ListaCircularInterfaz

class ListaCircularOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Lista Circular")

        # Elementos del frame
        self.titulo = Label(self, text="Lista Circular")
        self.lista_interfaz = ListaCircularInterfaz(self)
        self.botones_inferiores = BotonesInferiores(self, self.lista_interfaz)

class BotonesInferiores(PlantillaBotones):
    def __init__(self, master, lista_interfaz):
        super().__init__(master, lista_interfaz)
from tkinter import *
from frontend.lista_dobl_interfaz import ListaDobleInterfaz

class ListaDobEnOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Lista Doble Enlazada")

        # Elementos del frame
        self.titulo = Label(self, text="Lista Doble Enlazada")
        self.lista_doble_interfaz = ListaDobleInterfaz(self)
        self.botones_inferiores = BotonesInferiores(self, self.lista_doble_interfaz)


class BotonesInferiores(Frame):
    def __init__(self, lista_doble_interfaz):
        pass
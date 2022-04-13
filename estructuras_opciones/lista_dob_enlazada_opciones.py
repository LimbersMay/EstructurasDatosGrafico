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

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_doble_interfaz.grid(row=1, column=0)
        self.botones_inferiores.grid(row=2, column=0)


class BotonesInferiores(Frame):
    def __init__(self, lista_doble_interfaz):
        pass
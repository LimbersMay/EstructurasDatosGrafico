from tkinter import *
from estructuras.circular_list import CircularList
from .templates.lista_simple_template import ListaInterfaz
from .templates.botones_lineales_template import BotonesLista


class ListaCircularOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Lista Circular")

        # Elementos del frame
        self.titulo = Label(self, text="Lista Circular")
        self.lista_interfaz = ListaCircularInterfaz(self)
        self.botones_inferiores = BotonesInferiores(self, self.lista_interfaz)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_interfaz.grid(row=1, column=0)
        self.botones_inferiores.grid(row=2, column=0)


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


class BotonesInferiores(BotonesLista):
    def __init__(self, master, lista_interfaz):
        super().__init__(master, lista_interfaz)

        # Elementos del frame
        self.rotar_izquierda_button = Button(self, text="Rotar Izquierda", command=self.rotar_izquierda)
        self.rotar_derecha_button = Button(self, text="Rotar Derecha", command=self.rotar_derecha)

        # Posicionamiento de los elementos del frame
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.rotar_izquierda_button.grid(row=0, column=2)
        self.rotar_derecha_button.grid(row=0, column=3)

        self.insertar_inicio.grid(row=0, column=4)
        self.insertar_final.grid(row=0, column=5)

        self.eliminar_inicio.grid(row=0, column=6)
        self.eliminar_final.grid(row=0, column=7)

        self.buscar_button.grid(row=0, column=8)

    # Métodos de la lista
    def rotar_izquierda(self):
        self.lista_interfaz.rotar_izquierda()

    def rotar_derecha(self):
        self.lista_interfaz.rotar_derecha()

from tkinter import *
from estructuras.pila import Pila
from .templates.lista_simple_template import ListaInterfaz
from .templates.botones_lineales_template import BotonesBasicos


class PilaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de datos Pila")

        # Elementos del frame
        self.label_titulo = Label(self, text="Pila")
        self.pila_interfaz = PilaInterfaz(self)
        self.botones_inferiores = BotonesPila(self, self.pila_interfaz)

        # Posicionamiento de los elementos
        self.label_titulo.grid(row=0, column=0)
        self.pila_interfaz.grid(row=1, column=0)
        self.botones_inferiores.grid(row=2, column=0)


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


class BotonesPila(BotonesBasicos):
    def __init__(self, master, pila_interfaz):
        super().__init__(master, pila_interfaz)

        # Posicionamiento de los elementos del frame
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_button.grid(row=0, column=2)
        self.eliminar_button.grid(row=0, column=3)
        self.buscar_button.grid(row=0, column=4)

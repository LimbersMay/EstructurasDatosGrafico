from tkinter import *
from estructuras.cola import Cola
from .templates.lista_simple_template import ListaInterfaz
from .templates.botones_lineales_template import BotonesBasicos


class ColaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de dato Cola")

        # Atributos
        self.titulo = Label(self, text="Estructura de dato Cola")
        self.cola_interfaz = ColaInterfaz(self)
        self.botones_inferiores = BotonesCola(self, self.cola_interfaz)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.cola_interfaz.grid(row=1, column=0)
        self.botones_inferiores.grid(row=2, column=0)


class ColaInterfaz(ListaInterfaz):

    def __init__(self, master):
        super().__init__(master)

        self.lista = Cola()

    def insertar(self, elemento):
        self.lista.insertar(elemento)

        self.dibujar_lista()

    def eliminar(self):
        self.lista.eliminar()

        self.dibujar_lista()


class BotonesCola(BotonesBasicos):
    def __init__(self, master, cola_interfaz):
        super().__init__(master, cola_interfaz)

        # Posicionamiento de los elementos del frame
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_button.grid(row=0, column=2)
        self.eliminar_button.grid(row=0, column=3)
        self.buscar_button.grid(row=0, column=4)
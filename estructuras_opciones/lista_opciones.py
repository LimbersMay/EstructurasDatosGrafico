from tkinter import *
from estructuras_opciones.botones_template import BotonesLista
from frontend.lista_simple_interfaz import ListaSimpleInterfaz


class ListaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de datos Lista")

        # Elementos del frame
        self.titulo = Label(self, text="Lista simplemente enlazada")
        self.lista_interfaz = ListaSimpleInterfaz(self)
        self.botones_inferiores = BotonesInferiores(self, self.lista_interfaz)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_interfaz.grid(row=1, column=0)
        self.botones_inferiores.grid(row=2, column=0)


class BotonesInferiores(BotonesLista):
    def __init__(self, master, lista_interfaz):
        super().__init__(master, lista_interfaz)

        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_final.grid(row=0, column=2)
        self.insertar_inicio.grid(row=0, column=3)

        self.eliminar_final.grid(row=0, column=4)
        self.eliminar_inicio.grid(row=0, column=5)

        self.buscar_button.grid(row=0, column=6)
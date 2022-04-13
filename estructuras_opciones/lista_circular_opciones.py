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

        # Elementos del frame
        self.rotar_izquierda_button = Button(self, text="Rotar Izquierda")
        self.rotar_derecha_button = Button(self, text="Rotar Derecha")

        # Posicionamiento de los elementos del frame
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_button.grid(row=0, column=2)
        self.eliminar_button.grid(row=0, column=3)
        self.buscar_button.grid(row=0, column=4)

        self.rotar_izquierda_button.grid(row=0, column=5)
        self.rotar_derecha_button.grid(row=0, column=6)

        
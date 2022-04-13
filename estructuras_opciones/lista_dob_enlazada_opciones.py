from tkinter import *
from frontend.lista_dobl_interfaz import ListaDobEnlazadaInterfaz
from estructuras_opciones.operaciones_estructuras import BotonesLista

class ListaDobEnOpciones(Frame):

    # Variable estatica para el manejo de la lista

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Lista Doble Enlazada")

        # Elementos del frame
        self.titulo = Label(self, text="Lista Doble Enlazada")
        self.lista_interfaz = ListaDobEnlazadaInterfaz(self)
        self.botones_inferiores = BotonesInferiores(self, self.lista_interfaz)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_interfaz.grid(row=1, column=0)
        self.botones_inferiores.grid(row=2, column=0)


class BotonesInferiores(BotonesLista):

    def __init__(self, master, lista_interfaz):
        super().__init__(master, lista_interfaz)

        # Elementos del frame
        self.indice_label = Label(self, text="Indice: ")
        self.indice_entry = Entry(self)

        self.insertar_posicion_button = Button(self, text="Insertar en posicion", command=self.insertar_posicion)

        self.eliminar_posicion_button = Button(self, text="Eliminar en posicion", command=self.eliminar_posicion)

        # Posicionamiento de los elementos
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.indice_label.grid(row=0, column=2)
        self.indice_entry.grid(row=0, column=3)

        self.insertar_posicion_button.grid(row=0, column=4)
        self.eliminar_posicion_button.grid(row=0, column=5)

        self.insertar_final.grid(row=0, column=6)
        self.insertar_inicio.grid(row=0, column=7)

        self.eliminar_final.grid(row=0, column=8)
        self.eliminar_inicio.grid(row=0, column=9)

        self.buscar_button.grid(row=0, column=10)
    
    # Métodos de la lista
    def insertar_posicion(self):
        self.lista_interfaz.insertar_posicion(self.dato_entry.get(), int(self.indice_entry.get()))
    
    def eliminar_posicion(self):
        self.lista_interfaz.eliminar_por_posicion(int(self.indice_entry.get()))
from tkinter import *
from estructuras.double_linked_list import DoubleLinkedList
from .templates.inf_estructura_template import EstructuraInformacion
from .templates.lista_simple_template import ListaInterfaz
from .templates.botones_lineales_template import BotonesLista


class ListaDobEnOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Lista Doble Enlazada")

        # Estructura
        self.lista = DoubleLinkedList()

        # Elementos del frame
        self.titulo = Label(self, text="Lista Doble Enlazada")
        self.lista_dob_informacion = ListaDobInformacion(self, self.lista)
        self.lista_dob_interfaz = ListaDobEnlazadaInterfaz(self, self.lista, self.lista_dob_informacion)
        self.botones_inferiores = BotonesDobEnlazada(self, self.lista_dob_interfaz)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_dob_interfaz.grid(row=1, column=0)
        self.lista_dob_informacion.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)

# Clase que mostrará toda la información de la lista del lado derecho de la pantalla dentro de un frame
class ListaDobInformacion(EstructuraInformacion):
    def __init__(self, master, lista_dob_enlazada):
        super().__init__(master, lista_dob_enlazada)

        # Posicionamos todos los elementos
        self.titulo.grid(row=0, column=0)

        self.tamanio.grid(row=1, column=0, sticky=W)
        self.tope.grid(row=2, column=0, sticky=W)
        self.fondo.grid(row=3, column=0, sticky=W)


class ListaDobEnlazadaInterfaz(ListaInterfaz):

    def __init__(self, master, lista_dob_enlazada, lista_dob_informacion):
        super().__init__(master, lista_dob_enlazada, lista_dob_informacion)

    def insertar_posicion(self, data, posicion):
        self.lista.append_in_position(data, posicion)

        # Actualizamos la lista y el frame de información
        self.actualizar_informacion()
        self.dibujar_lista()

    def eliminar_por_posicion(self, posicion):
        self.lista.remove_node_position(posicion)

        # Actualizamos la lista y el frame de información
        self.actualizar_informacion()
        self.dibujar_lista()


class BotonesDobEnlazada(BotonesLista):

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

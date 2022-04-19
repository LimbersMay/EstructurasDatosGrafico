from tkinter import *
from estructuras.double_linked_list import DoubleLinkedList
from .templates.inf_estructura_template import EstructuraInformacion
from .templates.lista_simple_template import ListaInterfaz
from .templates.botones_lineales_template import BotonesLista


# Responsabilidad: Mostrar todos los elementos de la interfaz
class ListaDobEnOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Lista Doble Enlazada")

        # Estructura
        self.lista = DoubleLinkedList()

        # Manager encargada de controlar los elementos de la interfaz
        self.manager = Manager(self.lista)

        # Elementos del frame
        self.titulo = Label(self, text="Lista Doble Enlazada")
        self.lista_dob_informacion = ListaDobInformacion(self, self.manager)
        self.lista_dob_interfaz = ListaDobEnlazadaInterfaz(self, self.manager)
        self.botones_inferiores = BotonesDobEnlazada(self, self.manager)

        # Le indicamos al manager que elementos manejará
        self.manager.set_lista_dob_interfaz(self.lista_dob_interfaz)
        self.manager.set_lista_dob_informacion(self.lista_dob_informacion)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_dob_interfaz.grid(row=1, column=0)
        self.lista_dob_informacion.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)


# Responsabilidad: Manejar los elementos de la interfaz proporcionandoles acceso a la estructura
class Manager:
    def __init__(self, estructura, lista_dob_interfaz=None, lista_dob_informacion=None):
        self.estructura = estructura
        self.lista_dob_interfaz = lista_dob_interfaz
        self.lista_dob_informacion = lista_dob_informacion
    
    # Método para obtener la estructura de datos
    def get_estructura(self):
        return self.estructura

    # Método para que cuando se haga alguna modificación a la lista, la dibujemos
    # y además imprimamos su información
    def actualizar(self):
        self.lista_dob_interfaz.actualizar()
        self.lista_dob_informacion.actualizar()

    def set_lista_dob_interfaz(self, lista_dob_interfaz):
        self.lista_dob_interfaz = lista_dob_interfaz

    def set_lista_dob_informacion(self, lista_dob_informacion):
        self.lista_dob_informacion = lista_dob_informacion


# Responsabilidad: Mostrar toda la información de la lista
class ListaDobInformacion(EstructuraInformacion):
    def __init__(self, master, manager):
        super().__init__(master, manager)

        # Posicionamos todos los elementos
        self.titulo.grid(row=0, column=0)

        self.tamanio.grid(row=1, column=0, sticky=W)
        self.tope.grid(row=2, column=0, sticky=W)
        self.fondo.grid(row=3, column=0, sticky=W)


# Responsabilidad: Mostrar la lista enlazada en una interfaz gráfica
class ListaDobEnlazadaInterfaz(ListaInterfaz):

    def __init__(self, master, manager):
        super().__init__(master, manager)


# Responsabilidad: Manejar los botones de la lista para manipularla
class BotonesDobEnlazada(BotonesLista):

    def __init__(self, master, manager):
        super().__init__(master, manager)

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
        dato = self.dato_entry.get()
        indice = int(self.indice_entry.get())

        self.manager.get_estructura().append_in_position(dato, indice)
        self.manager.actualizar()

    def eliminar_posicion(self):
        indice = int(self.indice_entry.get())

        self.manager.get_estructura().remove_in_position(indice)
        self.manager.actualizar()

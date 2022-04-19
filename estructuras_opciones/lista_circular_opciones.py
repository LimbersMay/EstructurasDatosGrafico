from tkinter import *
from estructuras.circular_list import CircularList
from .templates.inf_estructura_template import EstructuraInformacion
from .templates.lista_simple_template import ListaInterfaz
from .templates.botones_lineales_template import BotonesLista


# Responsabilidad: Mostrar todos los elementos de la interfaz
class ListaCircularOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Lista Circular")

        # Estrucuta
        self.lista = CircularList()

        # Manager de los widgets
        self.manager = Manager(self.lista)

        # Elementos del frame
        self.titulo = Label(self, text="Lista Circular")
        self.informacion_lista = ListaCircularInformacion(self, self.manager)
        self.lista_interfaz = ListaCircularInterfaz(self, self.manager)
        self.botones_inferiores = BotonesCircular(self, self.manager)

        # Le indicamos al manager que elementos manejará
        self.manager.set_lista_interfaz(self.lista_interfaz)
        self.manager.set_lista_informacion(self.informacion_lista)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_interfaz.grid(row=1, column=0)
        self.informacion_lista.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)


# Responsabilidad: Manejar los elementos de la interfaz proporcionandoles acceso a la estructura
class Manager:
    def __init__(self, lista, lista_interfaz=None, lista_informacion=None):
        self.lista = lista
        self.lista_interfaz = lista_interfaz
        self.lista_informacion = lista_informacion

    # Método para obtener la estructura de datos
    def get_estructura(self):
        return self.lista

    # Método para que cuando se haga alguna modificación a la lista, la dibujemos
    # y además imprimamos su información
    def actualizar(self):
        self.lista_interfaz.actualizar()
        self.lista_informacion.actualizar()

    def set_lista_interfaz(self, lista_interfaz):
        self.lista_interfaz = lista_interfaz

    def set_lista_informacion(self, lista_informacion):
        self.lista_informacion = lista_informacion


# Responsabilidad: Mostrar la información de la lista circular
class ListaCircularInformacion(EstructuraInformacion):
    def __init__(self, master, manager):
        super().__init__(master, manager)

        # Posicionamos todos los elementos
        self.titulo.grid(row=0, column=0)

        self.tamanio.grid(row=1, column=0, sticky=W)
        self.tope.grid(row=2, column=0, sticky=W)
        self.fondo.grid(row=3, column=0, sticky=W)


# Responsabilidad: Mostrar la lista circular en una interfaz gráfica
class ListaCircularInterfaz(ListaInterfaz):

    def __init__(self, master, manager):
        super().__init__(master, manager)


# Responsabilidad: Manejar los botones inferiores para manipular la lista circular
class BotonesCircular(BotonesLista):
    def __init__(self, master, manager):
        super().__init__(master, manager)

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
        self.manager.get_estructura().move_left()
        self.manager.actualizar()

    def rotar_derecha(self):
        self.manager.get_estructura().move_right()
        self.manager.actualizar()
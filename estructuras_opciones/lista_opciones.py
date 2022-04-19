from tkinter import *
from estructuras.linked_list import LinkedList
from .templates.inf_estructura_template import EstructuraInformacion
from .templates.lista_simple_template import ListaInterfaz
from .templates.botones_lineales_template import BotonesLista


# Responsabilidad: Mostrar todos los elementos de la interfaz
class ListaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de datos Lista")

        # Estructura del frame
        self.lista = LinkedList()

        # Manager de los widgets
        self.manager = Manager(self.lista)

        # Elementos del frame
        self.titulo = Label(self, text="Lista simplemente enlazada")
        self.lista_informacion = ListaInformacion(self, self.manager)
        self.lista_interfaz = ListaSimpleInterfaz(self, self.manager)
        self.botones_inferiores = BotonesInferiores(self, self.manager)

        # Le indicamos al manager que elementos manejará
        self.manager.set_lista_interfaz(self.lista_interfaz)
        self.manager.set_lista_informacion(self.lista_informacion)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_interfaz.grid(row=1, column=0)
        self.lista_informacion.grid(row=1, column=1)
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


# Responsabilidad: Mostrar toda la información de la lista
class ListaInformacion(EstructuraInformacion):
    def __init__(self, master, manager):
        super().__init__(master, manager)

        # Posicionamos todos los elementos
        self.titulo.grid(row=0, column=0)

        self.tamanio.grid(row=1, column=0, sticky=W)
        self.tope.grid(row=2, column=0, sticky=W)
        self.fondo.grid(row=3, column=0, sticky=W)


# Responsabilidad: Mostrar la lista en una interfaz gráfica
class ListaSimpleInterfaz(ListaInterfaz):
    def __init__(self, master, manager):
        super().__init__(master, manager)


# Responsabilidad: Manejar los botones para manipular la lista
class BotonesInferiores(BotonesLista):
    def __init__(self, master, manager):
        super().__init__(master, manager)

        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_inicio.grid(row=0, column=2)
        self.insertar_final.grid(row=0, column=3)

        self.eliminar_final.grid(row=0, column=4)
        self.eliminar_inicio.grid(row=0, column=5)

        self.buscar_button.grid(row=0, column=6)

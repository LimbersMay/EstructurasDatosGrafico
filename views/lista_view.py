from tkinter import *
from estructuras.linked_list import LinkedList
from models.models import SimpleListModel
from controllers.controllers import SimpleListController
from .templates.inf_estructura_template import EstructuraInformacion
from .templates.estructura_lineal_template import EstructuraInterfaz
from .templates.botones_lineales_template import BotonesLista


# Responsabilidad: Mostrar todos los elementos de la interfaz
class ListaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de datos Lista")

        # Estructura del frame
        self.lista = LinkedList()

        # Definimos el modelo de datos de la lista
        self.modelo = SimpleListModel(self.lista)

        # Definimos el controlador de la lista
        self.controlador = SimpleListController(self.modelo, self)

        # Elementos del frame
        self.titulo = Label(self, text="Lista simplemente enlazada")
        self.lista_informacion = ListaInformacion(self)
        self.lista_interfaz = EstructuraSimpleInterfaz(self)
        self.botones_inferiores = BotonesInferiores(self, self.controlador)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_interfaz.grid(row=1, column=0)
        self.lista_informacion.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)

    # Método para actualizar toda la interfaz
    def actualizar(self, args):
        nodos_informacion = args[0]
        pila_informacion = args[1]
        nodo_buscado = args[2] if len(args) == 3 else None

        self.lista_informacion.actualizar(pila_informacion)
        self.lista_interfaz.actualizar(nodos_informacion, nodo_buscado)


# Responsabilidad: Mostrar toda la información de la lista
class ListaInformacion(EstructuraInformacion):
    def __init__(self, master):
        super().__init__(master)

        # Posicionamos todos los elementos
        self.titulo.grid(row=0, column=0)

        self.tamanio.grid(row=1, column=0, sticky=W)
        self.tope.grid(row=2, column=0, sticky=W)
        self.fondo.grid(row=3, column=0, sticky=W)


# Responsabilidad: Mostrar la lista en una interfaz gráfica
class EstructuraSimpleInterfaz(EstructuraInterfaz):
    def __init__(self, master):
        super().__init__(master)


# Responsabilidad: Manejar los botones para manipular la lista
class BotonesInferiores(BotonesLista):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)

        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_inicio.grid(row=0, column=2)
        self.insertar_final.grid(row=0, column=3)

        self.eliminar_final.grid(row=0, column=4)
        self.eliminar_inicio.grid(row=0, column=5)

        self.buscar_button.grid(row=0, column=6)

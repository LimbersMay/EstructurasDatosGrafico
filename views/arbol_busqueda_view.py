from tkinter import *
from estructuras.binary_search_tree import BinarySearchTree
from models.binary_tree_models import SearchBinaryTreeModel
from controllers.binary_tree_controllers import SearchBinaryTreeController
from .templates.inf_arbol_template import ArbolInformacion
from .templates.botones_arbol_template import BotonesArbol
from .templates.arbol_template import ArbolInterfaz


# Funcionalidad: Mostrar y posicionar todos los elementos de la interfaz
class ArbolBusquedaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # Estructura de dato que usaremos
        self.arbol = BinarySearchTree()

        # Definimos el modelo de los datos y el controlador
        self.modelo = SearchBinaryTreeModel(self.arbol)

        # Definimos el controlador de los datos y el modelo
        self.controlador = SearchBinaryTreeController(self.modelo, self)

        # Elementos del frame
        self.titulo = Label(self, text="Árbol de búsqueda")
        self.arbol_informacion = ArbolBusquedaInformacion(self)
        self.arbol_interfaz = ArbolBusquedaInterfaz(self)
        self.botones_arbol = BotonesArbolBusqueda(self, self.controlador)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.arbol_interfaz.grid(row=1, column=0)
        self.arbol_informacion.grid(row=1, column=1)
        self.botones_arbol.grid(row=2, column=0)

    # Funcionalidad: Actualizar la información del árbol
    def mostrar_arbol(self, args):
        self.arbol_interfaz.actualizar(args)
        self.arbol_informacion.actualizar(args)


# Responsabilidad: Mostrar el árbol en una interfaz gráfica
class ArbolBusquedaInformacion(ArbolInformacion):
    def __init__(self, master):
        super().__init__(master)

        # Posicionamos los elementos
        self.titulo.grid(row=0, column=0, columnspan=2, sticky=W)
        self.raiz.grid(row=1, column=0, sticky=W)
        self.tamanio.grid(row=2, column=0, sticky=W)
        self.profundidad.grid(row=3, column=0, sticky=W)


# Responsabilidad: Mostrar el árbol en una interfaz gráfica
class ArbolBusquedaInterfaz(ArbolInterfaz):
    def __init__(self, master):
        super().__init__(master)


# Responsabilidad: Manejar los botones para manipular el árbol
class BotonesArbolBusqueda(BotonesArbol):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)

        self.insertar = Button(self, text='Insertar', command=self.insertar)

        self.referencia_label = Label(self, text="Referencia: ")
        self.referencia_entry = Entry(self)

        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_raiz.grid(row=0, column=2)
        self.insertar.grid(row=0, column=3)

        self.eliminar.grid(row=0, column=4)
        self.buscar.grid(row=0, column=5)

    def insertar(self):
        self.controlador.insertar(self.dato_entry.get())

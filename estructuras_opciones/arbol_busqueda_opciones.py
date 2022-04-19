from tkinter import *
from estructuras.binary_search_tree import BinarySearchTree
from .templates.inf_arbol_template import ArbolInformacion
from .templates.botones_arbol_template import BotonesArbol
from .templates.arbol_template import ArbolInterfaz


# Funcionalidad: Mostrar y posicionar todos los elementos de la interfaz
class ArbolBusquedaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # Estructura de dato que usaremos
        self.arbol = BinarySearchTree()

        # Manager encargado de actualizar los frames
        self.manager = Manager(self.arbol)

        # Elementos del frame
        self.titulo = Label(self, text="Árbol de búsqueda")
        self.arbol_informacion = ArbolBusquedaInformacion(self, self.manager)
        self.arbol_interfaz = ArbolBusquedaInterfaz(self, self.manager)
        self.botones_arbol = BotonesArbolBusqueda(self, self.manager)

        # Le indicamos al manager de qué elementos de la interfaz se encargará
        self.manager.set_arbol_interfaz(self.arbol_interfaz)
        self.manager.set_arbol_informacion(self.arbol_informacion)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.arbol_interfaz.grid(row=1, column=0)
        self.arbol_informacion.grid(row=1, column=1)
        self.botones_arbol.grid(row=2, column=0)


# Responsabilidad: Darle funcionalidad los frames de la interfaz
class Manager:
    def __init__(self, arbol, arbol_interfaz=None, arbol_informacion=None):
        self.arbol = arbol
        self.arbol_interfaz = arbol_interfaz
        self.arbol_informacion = arbol_informacion

    # Método para indicarle al manager que ha sido modificada la estructura de datos, así que
    # Debemos dibujarla y actualizar el frame de información
    def actualizar(self):
        self.arbol_informacion.actualizar()
        self.arbol_interfaz.actualizar()

    def get_estructura(self):
        return self.arbol

    def set_arbol_interfaz(self, arbol_interfaz):
        self.arbol_interfaz = arbol_interfaz

    def set_arbol_informacion(self, arbol_informacion):
        self.arbol_informacion = arbol_informacion


# Responsabilidad: Mostrar el árbol en una interfaz gráfica
class ArbolBusquedaInformacion(ArbolInformacion):
    def __init__(self, master, manager):
        super().__init__(master, manager)

        # Posicionamos los elementos
        self.titulo.grid(row=0, column=0, columnspan=2, sticky=W)
        self.raiz.grid(row=1, column=0, sticky=W)
        self.tamanio.grid(row=2, column=0, sticky=W)
        self.profundidad.grid(row=3, column=0, sticky=W)


# Responsabilidad: Mostrar el árbol en una interfaz gráfica
class ArbolBusquedaInterfaz(ArbolInterfaz):
    def __init__(self, master, manager):
        super().__init__(master, manager)


# Responsabilidad: Manejar los botones para manipular el árbol
class BotonesArbolBusqueda(BotonesArbol):
    def __init__(self, master, manager):
        super().__init__(master, manager)

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
        self.manager.get_estructura().insert(self.dato_entry.get())
        self.manager.actualizar()
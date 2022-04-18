from tkinter import *
from estructuras.binary_search_tree import BinarySearchTree
from .templates.inf_arbol_template import ArbolInformacion
from .templates.botones_arbol_template import BotonesArbol
from .templates.arbol_template import ArbolInterfaz

class ArbolBusquedaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # Estructura de dato que usaremos
        self.arbol = BinarySearchTree()

        # Elementos del frame
        self.titulo = Label(self, text="Árbol de búsqueda")
        self.arbol_informacion = ArbolBusquedaInformacion(self, self.arbol)
        self.arbol_interfaz = ArbolBusquedaInterfaz(self, self.arbol, self.arbol_informacion)
        self.botones_arbol = BotonesArbolBusqueda(self, self.arbol_interfaz)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.arbol_interfaz.grid(row=1, column=0)
        self.arbol_informacion.grid(row=1, column=1)
        self.botones_arbol.grid(row=2, column=0)


# Clase que mostrará toda la información del árbol binario
class ArbolBusquedaInformacion(ArbolInformacion):
    def __init__(self, master, arbol_busqueda):
        super().__init__(master, arbol_busqueda)

        # Posicionamos los elementos
        self.titulo.grid(row=0, column=0, columnspan=2, sticky=W)
        self.raiz.grid(row=1, column=0, sticky=W)
        self.tamanio.grid(row=2, column=0, sticky=W)
        self.profundidad.grid(row=3, column=0, sticky=W)


class ArbolBusquedaInterfaz(ArbolInterfaz):
    def __init__(self, master, arbol_busqueda, arbol_informacion):
        super().__init__(master, arbol_busqueda, arbol_informacion)
    
    def insertar(self, elemento):
        self.arbol.insert(elemento)

        # Dibujamos el árbol y actualizamos la información del frame
        self.actualizar_informacion_frame()
        self.dibujar_arbol()


class BotonesArbolBusqueda(BotonesArbol):
    def __init__(self, master, arbol_interfaz):
        super().__init__(master, arbol_interfaz)

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
        self.arbol_interfaz.insertar(self.dato_entry.get())
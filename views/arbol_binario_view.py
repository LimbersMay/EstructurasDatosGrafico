from tkinter import *
from estructuras.binary_tree import BinaryTree
from .templates.inf_arbol_template import ArbolInformacion
from .templates.arbol_template import ArbolInterfaz
from .templates.botones_arbol_template import BotonesArbol


# Responsabilidad: Posicionar todos los elementos visibles en la ventana
class ArbolBinarioOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # Estructura utilizada
        self.arbol = BinaryTree()

        # Manager de la interfaz del árbol
        self.manager = Manager(self.arbol)

        master.title("Arbol binario")

        self.titulo = Label(self, text="Arbol Binario simple")
        self.arbol_informacion = ArbolBinarioInformacion(self, self.manager)
        self.arbol_interfaz = ArbolBinarioInterfaz(self, self.manager)
        self.botones_arbol = BotonesArbolBinario(self, self.manager)

        # Le indicamos al manager de qué elementos de la interfaz se encargará
        self.manager.set_arbol_interfaz(self.arbol_interfaz)
        self.manager.set_arbol_informacion(self.arbol_informacion)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.arbol_interfaz.grid(row=1, column=0)
        self.arbol_informacion.grid(row=1, column=1)
        self.botones_arbol.grid(row=2, column=0)


# Responsabilidad: Manejar los elementos de la interfaz proporcionandoles funcionalidad
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


# Responsabilidad: Mostrar toda la información del árbol (tamaño, altura, profundidad)
class ArbolBinarioInformacion(ArbolInformacion):
    def __init__(self, master, manager):
        super().__init__(master, manager)

        # Posicionamos los elementos
        self.titulo.grid(row=0, column=0, columnspan=2, sticky=W)
        self.raiz.grid(row=1, column=0, sticky=W)
        self.tamanio.grid(row=2, column=0, sticky=W)
        self.profundidad.grid(row=3, column=0, sticky=W)


# Responsabilidad: Mostrar el árbol en una interfaz gráfica
class ArbolBinarioInterfaz(ArbolInterfaz):
    def __init__(self, master, manager):
        super().__init__(master, manager)


# Responsabilidad: Manejar los botones para manipular la información del árbol
class BotonesArbolBinario(BotonesArbol):
    def __init__(self, master, manager):
        super().__init__(master, manager)

        self.insertar_derecha = Button(self, text="Insertar Derecha", command=self.insertar_derecha)
        self.insertar_izquierda = Button(self, text="Insertar Izquierda", command=self.insertar_izquierda)

        self.referencia_label = Label(self, text="Referencia: ")
        self.referencia_entry = Entry(self)

        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.referencia_label.grid(row=0, column=2)
        self.referencia_entry.grid(row=0, column=3)

        self.insertar_raiz.grid(row=0, column=4)

        self.insertar_derecha.grid(row=0, column=5)
        self.insertar_izquierda.grid(row=0, column=6)

        self.eliminar.grid(row=0, column=7)
        self.buscar.grid(row=0, column=8)

    def insertar_izquierda(self):
        dato = self.dato_entry.get()
        referencia = self.referencia_entry.get()

        self.manager.get_estructura().insert_left(dato, referencia)
        self.manager.actualizar()

    def insertar_derecha(self):
        dato = self.dato_entry.get()
        referencia = self.referencia_entry.get()

        self.manager.get_estructura().insert_right(dato, referencia)
        self.manager.actualizar()
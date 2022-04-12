from tkinter import *
from frontend.lista_interfaz import ListaInterfaz

class ListaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de datos Lista")

        # Elementos del frame
        self.titulo = Label(self, text="Lista simplemente enlazada")
        self.lista_interfaz = ListaInterfaz(self)
        self.botones_inferiores = BotonesInferiores(self, self.lista_interfaz)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_interfaz.grid(row=1, column=0)
        self.botones_inferiores.grid(row=2, column=0)

class BotonesInferiores(Frame):
    def __init__(self, master, lista_interfaz):
        Frame.__init__(self, master)

        # Recibimos la lista interfaz para poder acceder a los métodos de eliminar, insertar y demás
        self.lista_interfaz = lista_interfaz

        # Elementos del frame
        self.texto_dato = Label(self, text="Introduce un valor: ")
        self.dato_entry = Entry(self)

        self.insertar_final = Button(self, text="Insertar al final")
        self.insertar_inicio = Button(self, text="Insertar al inicio")

        self.eliminar_final = Button(self, text="Eliminar al final")
        self.eliminar_inicio = Button(self, text="Eliminar al inicio")

        self.buscar_button = Button(self, text="Buscar") 
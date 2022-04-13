from tkinter import *
from frontend.lista_simple_interfaz import ListaSimpleInterfaz


class ListaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de datos Lista")

        # Elementos del frame
        self.titulo = Label(self, text="Lista simplemente enlazada")
        self.lista_interfaz = ListaSimpleInterfaz(self)
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

        self.insertar_final = Button(self, text="Insertar al final", command=self.insertar_final)
        self.insertar_inicio = Button(self, text="Insertar al inicio", command=self.insertar_inicio)

        self.eliminar_final = Button(self, text="Eliminar al final", command=self.eliminar_final)
        self.eliminar_inicio = Button(self, text="Eliminar al inicio", command=self.eliminar_inicio)

        self.buscar_button = Button(self, text="Buscar", command=self.buscar)

        # Posicionamiento de los elementos
        self.texto_dato.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_final.grid(row=0, column=2)
        self.insertar_inicio.grid(row=0, column=3)

        self.eliminar_final.grid(row=0, column=4)
        self.eliminar_inicio.grid(row=0, column=5)

        self.buscar_button.grid(row=0, column=6)

    def insertar_final(self):
        self.lista_interfaz.insertar_final(self.dato_entry.get())

    def insertar_inicio(self):
        self.lista_interfaz.insertar_inicio(self.dato_entry.get())

    def eliminar_final(self):
        self.lista_interfaz.eliminar_final()

    def eliminar_inicio(self):
        self.lista_interfaz.eliminar_inicio()

    def buscar(self):
        self.lista_interfaz.buscar(self.dato_entry.get())

from tkinter import *


# Clase plantilla para los botones inferiores de todas los tipos de listas
class BotonesLista(Frame):

    def __init__(self, master, lista_interfaz):
        Frame.__init__(self, master)

        # Atributos
        self.lista_interfaz = lista_interfaz

        # Elementos del frame
        self.dato_label = Label(self, text="Valor: ")
        self.dato_entry = Entry(self)

        self.insertar_final = Button(self, text="Insertar al final", command=self.insertar_final)
        self.insertar_inicio = Button(self, text="Insertar al inicio", command=self.insertar_inicio)

        self.eliminar_final = Button(self, text="Eliminar al final", command=self.eliminar_final)
        self.eliminar_inicio = Button(self, text="Eliminar al inicio", command=self.eliminar_inicio)

        self.buscar_button = Button(self, text="Buscar", command=self.buscar)

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


class BotonesBasicos(Frame):
    def __init__(self, master, estructura_interfaz):
        Frame.__init__(self, master)

        self.estructura_interfaz = estructura_interfaz

        # Elementos del frame
        self.dato_label = Label(self, text="Valor: ")
        self.dato_entry = Entry(self)

        self.insertar_button = Button(self, text="Insertar", command=self.insertar)
        self.eliminar_button = Button(self, text="Eliminar", command=self.eliminar)
        self.buscar_button = Button(self, text="Buscar", command=self.buscar)

    # Métodos de la estructura (Pila o Cola)
    def insertar(self):
        self.estructura_interfaz.insertar(self.dato_entry.get())

    def eliminar(self):
        self.estructura_interfaz.eliminar()

    def buscar(self):
        self.estructura_interfaz.buscar(self.dato_entry.get())

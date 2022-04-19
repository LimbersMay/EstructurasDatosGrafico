from tkinter import *


# Clase plantilla para los botones inferiores de todas los tipos de listas
class BotonesLista(Frame):

    def __init__(self, master, manager):
        Frame.__init__(self, master)

        # Atributos
        self.manager = manager

        # Elementos del frame
        self.dato_label = Label(self, text="Valor: ")
        self.dato_entry = Entry(self)

        self.insertar_final = Button(self, text="Insertar al final", command=self.insertar_final)
        self.insertar_inicio = Button(self, text="Insertar al inicio", command=self.insertar_inicio)

        self.eliminar_final = Button(self, text="Eliminar al final", command=self.eliminar_final)
        self.eliminar_inicio = Button(self, text="Eliminar al inicio", command=self.eliminar_inicio)

        self.buscar_button = Button(self, text="Buscar", command=self.buscar)

    def insertar_final(self):
        self.manager.get_estructura().append(self.dato_entry.get())
        self.manager.actualizar()

    def insertar_inicio(self):
        self.manager.get_estructura().prepend(self.dato_entry.get())
        self.manager.actualizar()

    def eliminar_final(self):
        self.manager.get_estructura().remove_tail()
        self.manager.actualizar()

    def eliminar_inicio(self):
        self.manager.get_estructura().remove_head()
        self.manager.actualizar()

    def buscar(self):
        self.manager.get_estructura().search(self.dato_entry.get())
        self.manager.actualizar()


class BotonesBasicos(Frame):
    def __init__(self, master, manager):
        Frame.__init__(self, master)

        self.manager = manager

        # Elementos del frame
        self.dato_label = Label(self, text="Valor: ")
        self.dato_entry = Entry(self)

        self.insertar_button = Button(self, text="Insertar", command=self.insertar)
        self.eliminar_button = Button(self, text="Eliminar", command=self.eliminar)
        self.buscar_button = Button(self, text="Buscar", command=self.buscar)

    # Métodos de la estructura (Pila o Cola)
    def insertar(self):
        self.manager.get_estructura().insertar(self.dato_entry.get())
        self.manager.actualizar()

    def eliminar(self):
        self.manager.get_estructura().eliminar()
        self.manager.actualizar()

    def buscar(self):
        self.manager.get_estructura().search()
        self.manager.actualizar()

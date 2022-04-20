# Clase que almacenará una estructura y que contendrá todos sus atributos

from tkinter import *


class EstructuraInformacion(Frame):
    def __init__(self, master, manager):
        Frame.__init__(self, master)

        self.manager = manager

        # Variables cambiantes de los label
        self.tamanio_variable = StringVar(self)
        self.tope_variable = StringVar(self)
        self.fondo_variable = StringVar(self)

        self.config(bg="darkred", width=200, height=350)
        self.grid_propagate(False)

        # Elementos del frame
        self.titulo = Label(self, text="Información de la estructura", bg="darkred", fg="white")

        self.tamanio = Label(self, textvariable=self.tamanio_variable, bg="darkred", fg="white")
        self.tope = Label(self, textvariable=self.tope_variable, bg="darkred", fg="white")
        self.fondo = Label(self, textvariable=self.fondo_variable, bg="darkred", fg="white")

        # Enviamos valores por defecto
        self.tamanio_variable.set(f"Tamaño: 0")
        self.tope_variable.set("Tope: Ninguno")
        self.fondo_variable.set("Fondo: Ninguno")

    # Método para actualizar toda la información común de la estructura
    def actualizar(self):
        self.tamanio_variable.set(f"Tamaño: {self.manager.get_estructura().get_size()}")
        self.tope_variable.set(f"Tope: {self.manager.get_estructura().get_head()}")
        self.fondo_variable.set(f"Fondo: {self.manager.get_estructura().get_tail()}")
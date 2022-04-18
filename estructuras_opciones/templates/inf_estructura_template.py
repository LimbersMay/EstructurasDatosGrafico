# Clase que almacenará una estructura y que contendrá todos sus atributos

from tkinter import *


class EstructuraInformacion(Frame):
    def __init__(self, master, estructura):
        Frame.__init__(self, master)

        self.estructura = estructura

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
        self.set_tamanio(0)
        self.set_tope(None)
        self.set_fondo(None)

    # Métodos para enviar la información de la pila
    def set_tamanio(self, tamanio):
        self.tamanio_variable.set(f"Tamaño: {tamanio}")
    
    def set_tope(self, tope):
        self.tope_variable.set(f"Tope: {tope}")
    
    def set_fondo(self, fondo):
        self.fondo_variable.set(f"Fondo: {fondo}")
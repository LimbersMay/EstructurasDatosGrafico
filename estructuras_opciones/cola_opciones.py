from tkinter import *
from frontend.cola_interfaz import ColaInterfaz
from estructuras_opciones.operaciones_estructuras import BotonesBasicos

class ColaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de dato Cola")

        # Atributos
        self.titulo = Label(self, text="Estructura de dato Cola")
        self.cola_interfaz = ColaInterfaz(self)
        self.botones_inferiores = BotonesBasicos(self, self.cola_interfaz)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.cola_interfaz.grid(row=1, column=0)
        self.botones_inferiores.grid(row=2, column=0)
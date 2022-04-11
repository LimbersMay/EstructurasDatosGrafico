from tkinter import *

class Titulo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Configuraciones
        self.config(
            bg="#066163",
            width=400,
            height=50
        )

        # Partes del programa
        self.titulo = Label(self, text="Selecciona la estructura deseada", font=("rockwell", 15), bg="#066163", fg="white")

        # Posicionamiento
        self.titulo.grid(row=0, column=0)
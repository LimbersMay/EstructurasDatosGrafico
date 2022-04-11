from tkinter import *
from estructuras.pila.pila import Pila

class PilaInterfaz(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.pila = Pila()

        # Configuraciones de la ventana
        self.config(
            width = 400,
            height = 300,
            bg = 'brown',
        )

        self.grid_propagate(False)

        # Elementos de la ventana



        # Configuraciones de los elementos de la ventana



        # Posicionamiento de los elementos

    def dibujar_pila(self):

        self.pila.insertar(5)

        elementos_pila = self.pila.recorrer()

        # Creamos un frame por cada elemento
        for i in range(len(elementos_pila)):

            # Creamos un frame
            frame = Frame(self)

            # Posicionamiento del frame
            frame.grid(row=i, column=0)

            # Insertamos el elemento en el frame
            Label(frame, text=elementos_pila[i]).pack()
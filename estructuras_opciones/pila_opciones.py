from tkinter import *
from frontend.pila_interfaz import PilaInterfaz

class PilaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
    
        master.title("Estructura de datos Pila")

        # Elementos del frame
        self.label_titulo = Label(self, text="Pila")
        self.pila_interfaz = PilaInterfaz(self)
        self.botones_inferiores = BotonesInferiores(self, self.pila_interfaz)

        # Posicionamiento de los elementos
        self.label_titulo.grid(row=0, column=0)
        self.pila_interfaz.grid(row=1, column=0)
        self.botones_inferiores.grid(row=2, column=0)


class BotonesInferiores(Frame):

    def __init__(self, master, pila_interfaz):
        Frame.__init__(self, master)

        # Recibimos la pila interfaz para poder acceder a los métodos de eliminar, insertar y demás
        self.pila_interfaz = pila_interfaz

        # Elementos del frame
        self.texto_dato = Label(self, text="Introduce un valor: ")
        self.dato_entry = Entry(self)

        self.insertar_button = Button(self, text="Insertar", command=self.insertar)
        self.eliminar_button = Button(self, text="Eliminar", command=self.eliminar)
        self.buscar_button = Button(self, text="Buscar", command=self.buscar)

        # Posicionamiento de los elementos
        self.texto_dato.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_button.grid(row=0, column=2)
        self.eliminar_button.grid(row=0, column=3)
        self.buscar_button.grid(row=0, column=4)
    
    def insertar(self):
        self.pila_interfaz.insertar(self.dato_entry.get())
    
    def eliminar(self):
        self.pila_interfaz.eliminar()
    
    def buscar(self):
        self.pila_interfaz.buscar(self.dato_entry.get())
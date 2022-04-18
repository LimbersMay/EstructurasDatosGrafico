from tkinter import *
from estructuras.pila import Pila
from .templates.inf_estructura_template import EstructuraInformacion
from .templates.lista_simple_template import ListaInterfaz
from .templates.botones_lineales_template import BotonesBasicos


class PilaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de datos Pila")

        self.pila = Pila()

        # Elementos del frame
        self.label_titulo = Label(self, text="Pila")
        self.pila_informacion = PilaInformacion(self, self.pila)
        self.pila_interfaz = PilaInterfaz(self, self.pila, self.pila_informacion)
        self.botones_inferiores = BotonesPila(self, self.pila_interfaz)

        # Posicionamiento de los elementos
        self.label_titulo.grid(row=0, column=0)
        self.pila_interfaz.grid(row=1, column=0)
        self.pila_informacion.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)


class PilaInformacion(EstructuraInformacion):
    def __init__(self, master, estructura):
        super().__init__(master, estructura)

        self.maximo_variable = StringVar(self)

        # Máximo de elementos de la pila
        self.maximo = Label(self, textvariable=self.maximo_variable, bg="darkred", fg="white")

        # Posicionamos los elementos
        self.titulo.grid(row=0, column=0, sticky=W)

        self.maximo.grid(row=1, column=0, sticky=W)
        self.tamanio.grid(row=2, column=0, sticky=W)
        self.tope.grid(row=3, column=0, sticky=W)
        self.fondo.grid(row=4, column=0, sticky=W)

        # Enviamos el maximo por defecto
        self.set_maximo(0)

    # Método para actualizar el máximo de elementos de la pila
    def set_maximo(self, maximo):
        self.maximo_variable.set(f"Máximo: {maximo}")

class PilaInterfaz(ListaInterfaz):

    def __init__(self, master, estructura, estructura_informacion):
        super().__init__(master, estructura, estructura_informacion)

    def insertar(self, valor):
        self.lista.insertar(valor)

        self.actualizar_informacion()
        self.dibujar_lista()

    def eliminar(self):
        self.lista.eliminar()

        self.actualizar_informacion()
        self.dibujar_lista()

    def buscar(self, valor):
        self.dibujar_lista(valor)


class BotonesPila(BotonesBasicos):
    def __init__(self, master, pila_interfaz):
        super().__init__(master, pila_interfaz)

        # Posicionamiento de los elementos del frame
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_button.grid(row=0, column=2)
        self.eliminar_button.grid(row=0, column=3)
        self.buscar_button.grid(row=0, column=4)

from tkinter import *
from estructuras.cola import Cola
from .templates.inf_estructura_template import EstructuraInformacion
from .templates.lista_simple_template import ListaInterfaz
from .templates.botones_lineales_template import BotonesBasicos


class ColaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de dato Cola")

        # Estructura de dato que se utilizará en el programa
        self.cola = Cola()

        # Atributos
        self.titulo = Label(self, text="Estructura de dato Cola")
        self.cola_informacion = ColaInformacion(self, self.cola)
        self.cola_interfaz = ColaInterfaz(self, self.cola, self.cola_informacion)
        self.botones_inferiores = BotonesCola(self, self.cola_interfaz)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.cola_interfaz.grid(row=1, column=0)
        self.cola_informacion.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)


# Clase que contiene toda la información de la cola
class ColaInformacion(EstructuraInformacion):
    
    def __init__(self, master, estructura: Cola):
        super().__init__(master, estructura)

        self.estructura = estructura

        self.maximo_variable = StringVar(self)

        # Máximo de elementos de la cola
        self.maximo = Label(self, textvariable=self.maximo_variable, bg="darkred", fg="white")

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0, sticky=W)

        self.maximo.grid(row=1, column=0, sticky=W)
        self.tamanio.grid(row=2, column=0, sticky=W)
        self.tope.grid(row=3, column=0, sticky=W)
        self.fondo.grid(row=4, column=0, sticky=W)

        # Enviamos el maximo por defecto
        self.set_maximo(0)
    
    # Método para actualizar el máximo de elementos de la cola
    def set_maximo(self, maximo):
        self.maximo_variable.set(f"Máximo: {maximo}")


# Clase que contiene la interfaz de la cola
class ColaInterfaz(ListaInterfaz):

    def __init__(self, master, estructura, estructura_informacion):
        super().__init__(master, estructura, estructura_informacion)

    def insertar(self, elemento):
        self.lista.insertar(elemento)

        self.actualizar_informacion()
        self.dibujar_lista()

    def eliminar(self):
        self.lista.eliminar()
        
        self.actualizar_informacion()
        self.dibujar_lista()


# Clase que contiene los botones inferiores de la cola
class BotonesCola(BotonesBasicos):
    def __init__(self, master, cola_interfaz: ColaInterfaz):
        super().__init__(master, cola_interfaz)

        # Posicionamiento de los elementos del frame
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_button.grid(row=0, column=2)
        self.eliminar_button.grid(row=0, column=3)
        self.buscar_button.grid(row=0, column=4)
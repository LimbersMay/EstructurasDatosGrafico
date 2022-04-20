from tkinter import *
from estructuras.cola import Cola
from models.queue_model import QueueModel
from controllers.queue_controller import QueueController
from .templates.inf_estructura_template import EstructuraInformacion
from .templates.estructura_lineal_template import EstructuraInterfaz
from .templates.botones_lineales_template import BotonesBasicos


# Responsabilidad: Posicionar y mostrar todos los elementos de la interfaz
class ColaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de dato Cola")

        # Estructura de dato que se utilizará en el programa
        self.cola = Cola()

        # Definimos el modelo de datos
        self.modelo = QueueModel(self.cola)

        # Definimos el controlador de datos
        self.controlador = QueueController(self.modelo, self)

        # Atributos
        self.titulo = Label(self, text="Estructura de dato Cola")
        self.cola_informacion = ColaInformacion(self)
        self.cola_interfaz = ColaInterfaz(self)
        self.botones_inferiores = BotonesCola(self, self.controlador)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.cola_interfaz.grid(row=1, column=0)
        self.cola_informacion.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)

    # Método para actualizar toda la información de la vista
    def actualizar(self, args):
        nodos_informacion = args[0]
        pila_informacion = args[1]
        nodo_buscado = args[2] if len(args) == 3 else None

        self.cola_informacion.actualizar(pila_informacion)
        self.cola_interfaz.actualizar(nodos_informacion, nodo_buscado)


# Responsabilidad: Mostrar toda la información de la estructura de datos
class ColaInformacion(EstructuraInformacion):

    def __init__(self, master):
        super().__init__(master)

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
        self.maximo_variable.set('Máximo: 0')

    def actualizar(self, pila_informacion):
        super().actualizar(pila_informacion)
        self.maximo_variable.set(f"Máximo: {pila_informacion.get_max()}")


# Responsabilidad: Mostrar la cola en una interfaz gráfica
class ColaInterfaz(EstructuraInterfaz):

    def __init__(self, master):
        super().__init__(master)


# Responsabilidad: Manejar los botones para manipular la cola
class BotonesCola(BotonesBasicos):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)

        # Posicionamiento de los elementos del frame
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_button.grid(row=0, column=2)
        self.eliminar_button.grid(row=0, column=3)
        self.buscar_button.grid(row=0, column=4)

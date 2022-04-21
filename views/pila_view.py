from tkinter import *
from estructuras.pila import Pila
from controllers.stack_controller import StackController
from models.stack_model import StackModel
from .templates.inf_estructura_template import EstructuraInformacion
from .templates.estructura_lineal_template import EstructuraInterfaz
from .templates.botones_lineales_template import BotonesBasicos


# Responsabilidad: Mostrar todos los elementos visibles
class PilaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de datos Pila")

        # Atributos
        # Estructura de la clase
        self.pila = Pila()

        # Definimos el modelo y el controlador de la clase
        self.modelo = StackModel(self.pila)
        self.controlador = StackController(self.modelo, self)

        # Elementos del frame
        self.label_titulo = Label(self, text="Pila")
        self.pila_informacion = PilaInformacion(self, self.controlador)
        self.pila_interfaz = PilaInterfaz(self)
        self.botones_inferiores = BotonesPila(self, self.controlador)

        # Posicionamiento de los elementos
        self.label_titulo.grid(row=0, column=0)
        self.pila_interfaz.grid(row=1, column=0)
        self.pila_informacion.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)

    # Método de la view para actualizar todos los frames de la interfaz
    def actualizar(self, args):

        nodos_informacion = args[0]
        pila_informacion = args[1]
        nodo_buscado = args[2] if len(args) == 3 else None

        self.pila_informacion.actualizar(pila_informacion)
        self.pila_interfaz.actualizar(nodos_informacion, nodo_buscado)


# Responsabilidad: Mostrar toda la información de la pila
class PilaInformacion(EstructuraInformacion):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)

        self.maximo_variable = StringVar(self)

        # Máximo de elementos de la pila
        self.maximo = Label(self, textvariable=self.maximo_variable, bg="darkred", fg="white")

        # Posicionamos los elementos
        self.titulo.grid(row=0, column=0, sticky=E)

        self.maximo.grid(row=1, column=0, sticky=W+E)
        self.tamanio.grid(row=2, column=0, sticky=W+E)
        self.tope.grid(row=3, column=0, sticky=W+E)
        self.fondo.grid(row=4, column=0, sticky=W+E)

        # Parte inferior de la información
        self.separador.grid(row=5, column=0, sticky=W+E)

        self.titulo_inferior.grid(row=6, column=0, sticky=W+E)
        self.titulo_inferior2.grid(row=7, column=0, sticky=W+E)
        self.lista_opciones.grid(row=8, column=0, sticky=E)
        self.estructura_campo.grid(row=9, column=0, sticky=E)

        # Botones
        self.contenedor_botones.grid(row=10, column=0, sticky=E)

        # Enviamos el maximo por defecto
        self.maximo_variable.set(f"Máximo: 0")

    # Método para actualizar el máximo de elementos de la pila
    def actualizar(self, pila_informacion):
        super().actualizar(pila_informacion)

        self.maximo_variable.set(f"Máximo: {pila_informacion.get_max()}")


# Responsabilidad: Mostrar la pila en una interfaz gráfica
class PilaInterfaz(EstructuraInterfaz):

    def __init__(self, master):
        super().__init__(master)


# Responsabilidad: Manejar los botones de la pila para manipularla
class BotonesPila(BotonesBasicos):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)

        # Posicionamiento de los elementos del frame
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_button.grid(row=0, column=2)
        self.eliminar_button.grid(row=0, column=3)
        self.buscar_button.grid(row=0, column=4)

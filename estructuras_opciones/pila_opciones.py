from tkinter import *
from estructuras.pila import Pila
from .templates.inf_estructura_template import EstructuraInformacion
from .templates.lista_simple_template import ListaInterfaz
from .templates.botones_lineales_template import BotonesBasicos


# Responsabilidad: Mostrar todos los elementos visibles
class PilaOpciones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de datos Pila")

        # Atributos
        # Estructura de la clase
        self.pila = Pila()

        # Manager de la clase
        self.manager = Manager(self.pila)

        # Elementos del frame
        self.label_titulo = Label(self, text="Pila")
        self.pila_informacion = PilaInformacion(self, self.manager)
        self.pila_interfaz = PilaInterfaz(self, self.manager)
        self.botones_inferiores = BotonesPila(self, self.manager)

        # Le indicamos al manager los elementos que tiene que manejar
        self.manager.set_pila_interfaz(self.pila_interfaz)
        self.manager.set_pila_informacion(self.pila_informacion)

        # Posicionamiento de los elementos
        self.label_titulo.grid(row=0, column=0)
        self.pila_interfaz.grid(row=1, column=0)
        self.pila_informacion.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)


# Responsabilidad: Manejar los elementos de la interfaz proporcionandoles acceso a la estructura
class Manager:
    def __init__(self, pila, pila_interfaz=None, pila_informacion=None):
        self.pila = pila
        self.pila_interfaz = pila_interfaz
        self.pila_informacion = pila_informacion
    
    # Método para obtener la estructura de datos
    def get_estructura(self):
        return self.pila
    
    # Método para que cuando se haga alguna modificación a la pila, la dibujemos 
    # y además imprimamos su información
    def actualizar(self):
        self.pila_interfaz.actualizar()
        self.pila_informacion.actualizar()

    def set_pila_interfaz(self, pila_interfaz):
        self.pila_interfaz = pila_interfaz

    def set_pila_informacion(self, pila_informacion):
        self.pila_informacion = pila_informacion


# Responsabilidad: Mostrar toda la información de la pila
class PilaInformacion(EstructuraInformacion):
    def __init__(self, master, manager):
        super().__init__(master, manager)

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
        self.maximo_variable.set(f"Máximo: 0")

    # Método para actualizar el máximo de elementos de la pila
    def actualizar(self):
        super().actualizar()

        self.maximo_variable.set(f"Máximo: {self.manager.get_estructura().get_max()}")


# Responsabilidad: Mostrar la pila en una interfaz gráfica
class PilaInterfaz(ListaInterfaz):

    def __init__(self, master, manager):
        super().__init__(master, manager)


# Responsabilidad: Manejar los botones de la pila para manipularla
class BotonesPila(BotonesBasicos):
    def __init__(self, master, manager):
        super().__init__(master, manager)

        # Posicionamiento de los elementos del frame
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_button.grid(row=0, column=2)
        self.eliminar_button.grid(row=0, column=3)
        self.buscar_button.grid(row=0, column=4)

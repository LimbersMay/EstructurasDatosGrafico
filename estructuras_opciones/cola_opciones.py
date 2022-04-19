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

        # Manager que se encargará de controlar la interfaz
        self.manager = Manager(self.cola)

        # Atributos
        self.titulo = Label(self, text="Estructura de dato Cola")
        self.cola_informacion = ColaInformacion(self, self.manager)
        self.cola_interfaz = ColaInterfaz(self, self.manager)
        self.botones_inferiores = BotonesCola(self, self.manager)

        # Le enviamos al manager los widgets que se encargarán de actualizar
        self.manager.set_cola_informacion(self.cola_informacion)
        self.manager.set_cola_interfaz(self.cola_interfaz)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.cola_interfaz.grid(row=1, column=0)
        self.cola_informacion.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)


class Manager:
    def __init__(self, cola, cola_informacion=None, cola_interfaz=None):
        
        self.cola_informacion = cola_informacion
        self.cola_interfaz = cola_interfaz
        self.cola = cola

    # Método para obtener la estructura de datos
    def get_estructura(self):
        return self.cola
    
    # Método para indicarle al manager que ha sido modificada la estructura de datos, así que 
    # Debemos dibujarla y actualizar el frame de información
    def actualizar(self):
        self.cola_informacion.actualizar()
        self.cola_interfaz.actualizar()

    def set_cola_informacion(self, cola_informacion):
        self.cola_informacion = cola_informacion
    
    def set_cola_interfaz(self, cola_interfaz):
        self.cola_interfaz = cola_interfaz

# Clase que contiene toda la información de la cola
class ColaInformacion(EstructuraInformacion):
    
    def __init__(self, master, manager):
        super().__init__(master, manager)

        self.manager = manager

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
    
    def actualizar(self):
        super().actualizar()
        self.maximo_variable.set(f"Máximo: {self.manager.get_estructura().get_max()}")


# Clase que contiene la interfaz de la cola
class ColaInterfaz(ListaInterfaz):

    def __init__(self, master, manager):
        super().__init__(master, manager)


# Clase que contiene los botones inferiores de la cola
class BotonesCola(BotonesBasicos):
    def __init__(self, master, manager):
        super().__init__(master, manager)

        # Posicionamiento de los elementos del frame
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_button.grid(row=0, column=2)
        self.eliminar_button.grid(row=0, column=3)
        self.buscar_button.grid(row=0, column=4)
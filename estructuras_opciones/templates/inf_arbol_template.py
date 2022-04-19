from tkinter import *

class ArbolInformacion(Frame):
    def __init__(self, master, manager):
        super().__init__(master)

        # Configuración del frame
        self.config(width=200, height=350, bg="darkred")
        self.grid_propagate(False)

        # Variables de la clase
        self.manager = manager

        # Variables camibiantes de los label
        self.raiz_variable = StringVar(self)
        self.tamanio_variable = StringVar(self)
        self.profundidad_variable = StringVar(self)

        # Label de las variables
        self.titulo = Label(self, text="Información del árbol", bg="darkred", fg="white")

        self.raiz = Label(self, textvariable=self.raiz_variable, bg="darkred", fg="white")
        self.tamanio = Label(self, textvariable=self.tamanio_variable, bg="darkred", fg="white")
        self.profundidad = Label(self, textvariable=self.profundidad_variable, bg="darkred", fg="white")

        # Enviamos valores por defecto
        self.raiz_variable.set("Raíz: Ninguna")
        self.tamanio_variable.set("Tamaño: 0")
        self.profundidad_variable.set("Profundidad: 0")
    
    # Método para actualizar toda la información del árbol
    def actualizar(self):
        self.raiz_variable.set(f"Raíz: {self.manager.get_estructura().get_root()}")
        self.tamanio_variable.set(f"Tamaño: {self.manager.get_estructura().count_nodes()}")
        self.profundidad_variable.set(f"Profundidad: {self.manager.get_estructura().max_depth()}")

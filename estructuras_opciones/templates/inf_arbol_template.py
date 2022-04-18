from tkinter import *

class ArbolInformacion(Frame):
    def __init__(self, master, arbol):
        super().__init__(master)

        # Configuración del frame
        self.config(width=200, height=350, bg="darkred")
        self.grid_propagate(False)

        # Variables de la clase
        self.arbol = arbol

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
        self.set_raiz(None)
        self.set_tamanio(0)
        self.set_profundidad(0)
    
    # Métodos para enviar la información del árbol
    def set_raiz(self, raiz):
        self.raiz_variable.set(f"Raíz: {raiz}")
    
    def set_tamanio(self, tamanio):
        self.tamanio_variable.set(f"Tamaño: {tamanio}")
    
    def set_profundidad(self, profundidad):
        self.profundidad_variable.set(f"Profundidad: {profundidad}")
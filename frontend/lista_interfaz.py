# Clase que será la plantilla para todas las listas
# Contendrá las operaciones básicas de una lista, cada lista agregará sus propias funcionalidades adicionales
from tkinter import Frame


class ListaInterfaz(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
# Clase que almacenará una estructura y que contendrá todos sus atributos
from tkinter import *
from tkinter import ttk


class EstructuraInformacion(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Variables cambiantes de los label
        self.tamanio_variable = StringVar(self)
        self.tope_variable = StringVar(self)
        self.fondo_variable = StringVar(self)

        self.config(bg="darkred", width=200, height=350)
        self.grid_propagate(False)

        # Elementos del frame
        self.titulo = Label(self, text="Información de la estructura")

        self.tamanio = Label(self, textvariable=self.tamanio_variable)
        self.tope = Label(self, textvariable=self.tope_variable)
        self.fondo = Label(self, textvariable=self.fondo_variable)

        # Parte baja de las opciones
        self.separador = Label(self, text="", bg="darkred")
        self.titulo_inferior = Label(self, text="Opciones adicionales")
        self.titulo_inferior2 = Label(self, text="Seleccionar estructura")
        self.lista_opciones = ttk.Combobox(self, values=["Lista", "Cola", "Pila", "Pila con cola"], state="readonly")
        self.estructura_campo = Entry(self, width=23)

        # Contenedor de los botones
        self.contenedor_botones = Frame(self, bg="darkred")

        self.cargar_btn = Button(self.contenedor_botones, text="Cargar")
        self.guardar_btn = Button(self.contenedor_botones, text="Guardar")
        self.eliminar_btn = Button(self.contenedor_botones, text="Eliminar")

        # Posicionamiento de los botones en el contenedor
        self.cargar_btn.grid(row=0, column=0)
        self.guardar_btn.grid(row=0, column=1)
        self.eliminar_btn.grid(row=0, column=2)

        # Aplicamos estilos a los elementos
        self.aplicar_estilo(self.titulo)
        self.aplicar_estilo(self.tamanio)
        self.aplicar_estilo(self.tope)
        self.aplicar_estilo(self.fondo)
        self.aplicar_estilo(self.separador)
        self.aplicar_estilo(self.titulo_inferior)
        self.aplicar_estilo(self.titulo_inferior2)
        self.aplicar_estilo(self.cargar_btn)
        self.aplicar_estilo(self.guardar_btn)
        self.aplicar_estilo(self.eliminar_btn)

        self.titulo.config(font=("Arial", 10))
        self.titulo_inferior.config(font=("Arial", 10))

        # Enviamos valores por defecto
        self.tamanio_variable.set(f"Tamaño: 0")
        self.tope_variable.set("Tope: Ninguno")
        self.fondo_variable.set("Fondo: Ninguno")

    # Método para aplicar estilo a todos los elementos
    def aplicar_estilo(self, elemento):
        elemento.config(bg="darkred", fg="white")

    # Método para actualizar toda la información común de la estructura
    def actualizar(self, estructura_informacion):
        self.tamanio_variable.set(f"Tamaño: {estructura_informacion.get_size()}")
        self.tope_variable.set(f"Tope: {estructura_informacion.get_head()}")
        self.fondo_variable.set(f"Fondo: {estructura_informacion.get_tail()}")

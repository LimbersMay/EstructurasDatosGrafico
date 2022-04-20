from tkinter import *

from views.arbol_binario_view import ArbolBinarioOpciones
from views.arbol_busqueda_view import ArbolBusquedaOpciones
from views.cola_view import ColaOpciones
from views.lista_circular_view import ListaCircularOpciones
from views.lista_dob_enlazada_view import ListaDobEnOpciones
from views.lista_view import ListaOpciones
from views.pila_view import PilaOpciones


class Botones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # Elementos del frame

        # Botón iniciar el frame del árbol
        self.arbol_boton = Button(self, text="Arbol", command=lambda:self.iniciar_ventana(ArbolBinarioOpciones))

        # Botón iniciar el frame del arbol de busqueda
        self.arbol_busqueda_boton = Button(self, text="Arbol de Busqueda", command=lambda:self.iniciar_ventana(ArbolBusquedaOpciones))

        # Botón iniciar el frame de cola
        self.cola_boton = Button(self, text="Cola", command=lambda:self.iniciar_ventana(ColaOpciones))

        # Botón iniciar el frame de la lista circular
        self.lista_circular = Button(self, text="Lista Circular", command=lambda:self.iniciar_ventana(ListaCircularOpciones))

        # Botón iniciar el frame de la lista doblemente enlazada
        self.lista_doble = Button(self, text="Lista Doble", command=lambda:self.iniciar_ventana(ListaDobEnOpciones))

        # Botón iniciar el frame de la lista simplemente enlazada
        self.lista_simple = Button(self, text="Lista Simple", command=lambda:self.iniciar_ventana(ListaOpciones))

        # Botón iniciar el frame de la pila
        self.pila_boton = Button(self, text="Pila", command=lambda:self.iniciar_ventana(PilaOpciones))
    
        # Configuraciones de los botones
        self.aplicar_configuracion(self.arbol_boton)
        self.aplicar_configuracion(self.arbol_busqueda_boton)
        self.aplicar_configuracion(self.cola_boton)
        self.aplicar_configuracion(self.lista_circular)
        self.aplicar_configuracion(self.lista_doble)
        self.aplicar_configuracion(self.lista_simple)
        self.aplicar_configuracion(self.pila_boton)

        # Posicionamiento
        self.arbol_boton.grid(row=0, column=0)
        self.arbol_busqueda_boton.grid(row=1, column=0)
        self.cola_boton.grid(row=2, column=0)
        self.lista_circular.grid(row=3, column=0)
        self.lista_doble.grid(row=4, column=0)
        self.lista_simple.grid(row=5, column=0)
        self.pila_boton.grid(row=6, column=0)
    

    def aplicar_configuracion(self, boton):
        boton.config(
            bg="#383838",
            width=20,
            height=1,
            font=("rockwell", 12),
            fg="white"
        )
    
    def iniciar_ventana(self, estructura):
        root = Toplevel()
        ventana = estructura(root)
        ventana.pack()
        root.mainloop()
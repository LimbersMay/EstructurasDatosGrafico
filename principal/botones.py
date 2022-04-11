from tkinter import *

class Botones(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # Elementos del frame

        # Botón iniciar el frame del árbol
        self.arbol_boton = Button(self, text="Arbol", command=self.iniciar_ventana_arbol)

        # Botón iniciar el frame del arbol de busqueda
        self.arbol_busqueda_boton = Button(self, text="Arbol de Busqueda", command=self.iniciar_ventana_arbol_busqueda)

        # Botón iniciar el frame de cola
        self.cola_boton = Button(self, text="Cola", command=self.iniciar_ventana_cola)

        # Botón iniciar el frame de la lista circular
        self.lista_circular = Button(self, text="Lista Circular", command=self.iniciar_ventana_lista_circular)

        # Botón iniciar el frame de la lista doblemente enlazada
        self.lista_doble = Button(self, text="Lista Doble", command=self.iniciar_ventana_lista_doble)

        # Botón iniciar el frame de la lista simplemente enlazada
        self.lista_simple = Button(self, text="Lista Simple", command=self.iniciar_ventana_lista_simple)

        # Botón iniciar el frame de la pila
        self.pila_boton = Button(self, text="Pila", command=self.iniciar_ventana_pila)
    
        # Configuraciones de los botones

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
            bg="#066163",
            width=10,
            height=2,
            font=("rockwell", 15),
            fg="white"
        )
    
    def iniciar_ventana_arbol(self):
        pass

    def iniciar_ventana_arbol_busqueda(self):
        pass

    def iniciar_ventana_cola(self):
        pass

    def iniciar_ventana_lista_circular(self):
        pass

    def iniciar_ventana_lista_doble(self):
        pass

    def iniciar_ventana_lista_simple(self):
        pass

    def iniciar_ventana_pila(self):
        pass
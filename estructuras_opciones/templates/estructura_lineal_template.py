# Clase que será la plantilla para todas las listas
# Contendrá las operaciones básicas de una lista, cada lista agregará sus propias funcionalidades adicionales
from tkinter import *


class EstructuraInterfaz(Frame):

    def __init__(self, master, manager):
        Frame.__init__(self, master)

        self.lista = manager.get_estructura()  # Nosotros definimos qué tipo de estructura usaremos
        self.lista_frames = []

        # Configuraciones de la ventana
        self.config(width=1000, height=350, bg="#146356")
        self.grid_propagate(False)

        self.rowconfigure(0, weight=1)
    
    def actualizar(self):
        self.dibujar_lista()

    def dibujar_lista(self, valor_buscado=None):
        # Eliminamos los frames de la lista
        for frame in self.lista_frames:
            frame.destroy()

        # Limpiamos la lista de frames
        self.lista_frames.clear()

        # Por cada nodo de la lista, se crea un frame
        for i in range(self.lista.get_size()):

            nuevo_frame = Frame(self, width=50, height=50, bg='#141E27', highlightbackground="black",
                                highlightthickness=1)

            self.lista_frames.append(nuevo_frame)

            # Se agrega el texto y la referencia del nodo al frame
            texto = Label(nuevo_frame, text=self.lista.search_position_node(i).data, bg='#141E27', fg='white',
                          font=('Arial', 20))
            referencia = Label(nuevo_frame, text=id(self.lista.search_position_node(i)), bg='#141E27', fg='white',
                               font=('Arial', 10))

            # Comprobamos si estamos en el primer nodo
            if i == 0:
                nuevo_frame.config(bg='#003638')
                texto.config(bg='#003638')
                referencia.config(bg='#003638')

            # Comprobamos si estamos en el último nodo
            if i == self.lista.get_size() - 1:
                nuevo_frame.config(bg='#006778')
                texto.config(bg='#006778')
                referencia.config(bg='#006778')

            # Comprobamos si el nodo es el que estamos buscando
            if self.lista.search_position_node(i).buscado:
                nuevo_frame.config(bg='#541212')
                texto.config(bg='#541212')
                referencia.config(bg='#541212')

                self.lista.search_position_node(i).set_buscado(False)

            # Los empaquetamos
            texto.grid(row=0, column=0)
            referencia.grid(row=1, column=0)

        # Posicionamos los frames en el medio de la ventana, uno a la derecha del otro
        for i in range(len(self.lista_frames)):
            self.lista_frames[i].grid(row=0, column=i, sticky=W)

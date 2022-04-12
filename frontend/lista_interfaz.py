from tkinter import *

from matplotlib.pyplot import text
from estructuras.lista_enlazada.linked_list import LinkedList

class ListaInterfaz(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lista = LinkedList()

        # Configuraciones de la ventana
        self.config(width=800, height=350)
        self.grid_propagate(False)

        self.rowconfigure(0, weight=1)
    
    def dibujar_lista(self):        
        lista_frames = []

        # Por cada nodo de la lista, se crea un frame
        for i in range(self.lista._size):
            nuevo_frame = Frame(self, width=50, height=50, bg='red', highlightbackground="black", highlightthickness=1)
            lista_frames.append(nuevo_frame)
            
            # Se agrega el texto y la referencia del nodo al frame
            texto = Label(nuevo_frame, text=self.lista.search_position_node(i).data, bg='red')
            referencia = Label(nuevo_frame, text=id(self.lista.search_position_node(i)), bg='red')
            
            # Los empaquetamos
            texto.grid(row=0, column=0)
            referencia.grid(row=1, column=0)
        
        # Posicionamos los frames en el medio de la ventana, uno a la derecha del otro
        for i in range(len(lista_frames)):
            lista_frames[i].grid(row=0, column=i, sticky=W)
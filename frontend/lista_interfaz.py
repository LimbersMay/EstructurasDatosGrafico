from tkinter import *

from matplotlib.pyplot import text
from estructuras.lista_enlazada.linked_list import LinkedList

class ListaInterfaz(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lista = LinkedList()
        self.lista_frames = []

        # Configuraciones de la ventana
        self.config(width=800, height=350)
        self.grid_propagate(False)

        self.rowconfigure(0, weight=1)
    
    def dibujar_lista(self, valor_buscado=None):      
        # Eliminamos los frames de la lista
        for frame in self.lista_frames:
            frame.destroy()
        
        # Limpiamos la lista de frames
        self.lista_frames.clear()

        # Bandera para comprobar que ya hemos buscado el elemento 
        buscado = False

        # Por cada nodo de la lista, se crea un frame
        for i in range(self.lista._size):

            nuevo_frame = Frame(self, width=50, height=50, bg='#141E27', highlightbackground="black", highlightthickness=1)

            self.lista_frames.append(nuevo_frame)
            
            # Se agrega el texto y la referencia del nodo al frame
            texto = Label(nuevo_frame, text=self.lista.search_position_node(i).data, bg='#141E27', fg='white', font=('Arial', 20))
            referencia = Label(nuevo_frame, text=id(self.lista.search_position_node(i)), bg='#141E27', fg='white', font=('Arial', 10))

            # Comprobamos si estamos en el primer nodo
            if i == 0:
                nuevo_frame.config(bg='#003638')
                texto.config(bg='#003638')
                referencia.config(bg='#003638')
            
            # Comprobamos si estamos en el último nodo
            if i == self.lista._size - 1:
                nuevo_frame.config(bg='#006778')
                texto.config(bg='#006778')
                referencia.config(bg='#006778')
            
            # Comprobamos si el valor buscado es el nodo actual
            if self.lista.search_position_node(i).data == valor_buscado and not buscado:
                nuevo_frame.config(bg='#541212')
                texto.config(bg='#541212')
                referencia.config(bg='#541212')

                buscado = True
            
            # Los empaquetamos
            texto.grid(row=0, column=0)
            referencia.grid(row=1, column=0)
        
        # Posicionamos los frames en el medio de la ventana, uno a la derecha del otro
        for i in range(len(self.lista_frames)):
            self.lista_frames[i].grid(row=0, column=i, sticky=W)
    
    def insertar_inicio(self, data):
        # Insertamos el nodo en la lista
        self.lista.prepend(data)

        # Dibujamos la lista
        self.dibujar_lista()
    
    def insertar_final(self, data):
        self.lista.append(data)

        # Dibujamos la lista
        self.dibujar_lista()
    
    def eliminar_inicio(self):
        self.lista.remove_head()

        # Dibujamos la lista
        self.dibujar_lista()
    
    def eliminar_final(self):
        self.lista.remove_tail()

        # Dibujamos la lista
        self.dibujar_lista()
    
    def buscar(self, valor):
        self.dibujar_lista(valor)
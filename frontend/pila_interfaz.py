from tkinter import *
from estructuras.pila.pila import Pila

class PilaInterfaz(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.pila = Pila()

        # Configuraciones de la ventana

        # Elementos de la ventana
        self.canvas = Canvas(self, width=800, height=350, bg='darkred')



        # Configuraciones de los elementos de la ventana



        # Posicionamiento de los elementos
        self.canvas.grid(row=1, column=0)

    def dibujar_pila(self, buscar_elemento=None):
        elementos_pila = self.pila.recorrer()

        # We draw rectangles in horizontal for each element in the stack and we draw the top element in red color and the rest in blue color and we put the value of the element in the rectangle and we draw it in the center of the rectangle.

        bandera = False # Bandera para saber si el elemento que estamos buscando esta en la pila
        
        for i in range(len(elementos_pila)):
            node_reference = id(self.pila.buscar_nodo(elementos_pila[i]))

            if i == 0:
                self.canvas.create_rectangle(100, 100, 200, 200, fill='red')
                self.canvas.create_text(150, 140, text=elementos_pila[i], fill='white', font=('Arial', 20))
                self.canvas.create_text(150, 170, text=node_reference, fill='white', font=('Arial', '10'))

            else:
                
                # Si el elemento en la posición no es la que buscamos, lo dibujamos en azul
                if not buscar_elemento == elementos_pila[i] or bandera:
                    self.canvas.create_rectangle(100 + (i * 100), 100, 200 + (i * 100), 200, fill='blue')

                    # We draw the value of the element in the center of the rectangle and we put the reference of the node under the value of the element.
                    self.canvas.create_text(150 + (i * 100), 140, text=elementos_pila[i], fill='white', font=('Arial', '20'))
                    self.canvas.create_text(150 + (i * 100), 170, text=node_reference, fill='white', font=('Arial', '10'))
                
                # Si el elemento en la posición es la que buscamos, lo dibujamos de azul
                if buscar_elemento == elementos_pila[i] and not bandera:
                    self.canvas.create_rectangle(100 + (i * 100), 100, 200 + (i * 100), 200, fill='#062C30')

                    self.canvas.create_text(150 + (i * 100), 140, text=elementos_pila[i], fill='white', font=('Arial', '20'))
                    self.canvas.create_text(150 + (i * 100), 170, text=node_reference, fill='white', font=('Arial', '10'))

                    bandera = True
    
    def insertar(self, valor):
        self.pila.insertar(valor)
        
        # Borramos todos los elementos que hay en el canvas
        self.canvas.delete("all")

        # Dibujamos la pila
        self.dibujar_pila()

    def eliminar(self):
        self.pila.eliminar()

        # Borramos todos los elementos que hay en el canvas
        self.canvas.delete("all")

        # Dibujamos la pila
        self.dibujar_pila()
    
    def buscar(self, valor):
        # Borramos todos los elementos que hay en el canvas
        self.canvas.delete("all")

        # Dibujamos la pila
        self.dibujar_pila(valor)
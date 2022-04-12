from tkinter import *
from estructuras.pila.pila import Pila

class PilaInterfaz(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.pila = Pila()

        # Configuraciones de la ventana
        self.config(
            width = 800,
            height = 500,
            bg = 'brown',
        )

        self.grid_propagate(False)

        # Elementos de la ventana
        self.canvas = Canvas(self, width=800, height=350, bg='darkred')



        # Configuraciones de los elementos de la ventana



        # Posicionamiento de los elementos
        self.canvas.grid(row=1, column=0)

    def dibujar_pila(self, buscar_elemento=None):

        self.pila.insertar(5)
        self.pila.insertar(4)
        self.pila.insertar(3)
        self.pila.insertar(2)
        self.pila.insertar(1)

        elementos_pila = self.pila.recorrer()

        # We draw rectangles in horizontal for each element in the stack and we draw the top element in red color and the rest in blue color and we put the value of the element in the rectangle and we draw it in the center of the rectangle.
        for i in range(len(elementos_pila)):
            node_reference = id(self.pila.buscar_nodo(elementos_pila[i]))
            if i == 0:
                self.canvas.create_rectangle(100, 100, 200, 200, fill='red')
                self.canvas.create_text(150, 150, text=elementos_pila[i], fill='white')
            else:
                
                if not buscar_elemento == elementos_pila[i]:
                    self.canvas.create_rectangle(100 + (i * 100), 100, 200 + (i * 100), 200, fill='blue')

                    # We draw the value of the element in the center of the rectangle and we put the reference of the node under the value of the element.
                    self.canvas.create_text(150 + (i * 100), 140, text=elementos_pila[i], fill='white', font=('Arial', '10'))
                    self.canvas.create_text(150 + (i * 100), 170, text=node_reference, fill='white', font=('Arial', '10'))
                
                if buscar_elemento == elementos_pila[i]:
                    self.canvas.create_rectangle(100 + (i * 100), 100, 200 + (i * 100), 200, fill='green')

                    self.canvas.create_text(150 + (i * 100), 150, text=elementos_pila[i], fill='white', font=('Arial', '10'))
                    self.canvas.create_text(150 + (i * 100), 170, text=node_reference, fill='white', font=('Arial', '10'))
    
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
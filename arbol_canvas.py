from tkinter import *
from PIL import ImageTk, Image

from estructuras.binary_tree import BinaryTree


class ArbolInterfaz(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Elementos del frame
        self.config(width=1000, height=350)

        self.arbol: BinaryTree = None

        self.canvas = Canvas(self, width=1000, height=350)
        self.canvas.pack()

        self.coordenadas_raiz = [
            500, 0,
            550, 50,
        ]

        # 500 -> 490 -> (10)
        # 550 -> 530 -> (20), 50 -> 30 -> (20)

        # 1. 500 - 2.5 = 497.5
        # 1. 550 - 5 = 545, 50 - 5 = 45

        # 2. 497.5 - 2.5 = 495
        # 2. 545 - 5 = 540, 45 - 5 = 40

        self.separacion = 0

    def dibujar_arbol(self, *args):
        nodo = self.arbol.get_root_reference() if len(args) == 0 else args[0]
        coordenadas = self.coordenadas_raiz if len(args) == 0 else args[1]
        separacion = self.separacion if len(args) == 0 else args[2]

        if nodo is not None:
            if nodo.is_leaf():
                # Dibujamos el nodo
                self.canvas.create_oval(coordenadas[0], coordenadas[1],
                                        coordenadas[2], coordenadas[3],
                                        fill="green")

                # Imprimimos el valor del nodo en el centro del nodo
                self.canvas.create_text(coordenadas[0] + (coordenadas[2] - coordenadas[0]) / 2,
                                        coordenadas[1] + (coordenadas[3] - coordenadas[1]) / 2,
                                        text=str(nodo.get_data()))

            else:
                # Obtenemos las coordenadas del nodo izquierdo
                # Creamos un nuevo nodo con las coordenadas del nodo izquierdo
                coordenadas_nodo_izquierdo = [
                    coordenadas[0] - 160 + separacion,
                    coordenadas[1] + 50,
                    (coordenadas[2] - 160 + separacion) - 4,
                    (coordenadas[3] + 50) - 4,
                ]

                coordenadas_nodo_derecho = [
                    coordenadas[0] + 160 - separacion,
                    coordenadas[1] + 50,
                    (coordenadas[2] + 160 - separacion) - 4,
                    (coordenadas[3] + 50) - 4,
                ]

                # Comprobamos que tenga un nodo izquierdo
                if nodo.get_left() is not None:
                    # Dibujamos una linea del punto medio del ovalo del nodo actual al punto medio del ovalo del nodo
                    # izquierdo
                    self.canvas.create_line(coordenadas[0] + (coordenadas[2] - coordenadas[0]) / 2,
                                            coordenadas[1] + (coordenadas[3] - coordenadas[1]) / 2,
                                            coordenadas_nodo_izquierdo[0] + (
                                                    coordenadas_nodo_izquierdo[2] - coordenadas_nodo_izquierdo[
                                                0]) / 2,
                                            coordenadas_nodo_izquierdo[1] + (
                                                    coordenadas_nodo_izquierdo[3] - coordenadas_nodo_izquierdo[
                                                1]) / 2,
                                            arrow=LAST, fill="black")

                # Comprobamos que tenga un nodo derecho
                if nodo.get_right() is not None:
                    # Dibujamos una linea del punto medio del ovalo del nodo actual al punto medio del ovalo del nodo derecho
                    self.canvas.create_line(coordenadas[0] + (coordenadas[2] - coordenadas[0]) / 2,
                                            coordenadas[1] + (coordenadas[3] - coordenadas[1]) / 2,
                                            coordenadas_nodo_derecho[0] + (
                                                    coordenadas_nodo_derecho[2] - coordenadas_nodo_derecho[0]) / 2,
                                            coordenadas_nodo_derecho[1] + (
                                                    coordenadas_nodo_derecho[3] - coordenadas_nodo_derecho[1]) / 2,
                                            arrow=LAST, fill="black")

                # Escribimos encima de las flechas el valor del nodo y nuestro nodo

                # En caso de tener hijos, dibujamos ambos nodos, los dibujamos encima de las flechas
                self.canvas.create_oval(coordenadas[0], coordenadas[1],
                                        coordenadas[2], coordenadas[3],
                                        fill="green")

                # Imprimimos el valor del nodo en el centro del nodo
                self.canvas.create_text(coordenadas[0] + (coordenadas[2] - coordenadas[0]) / 2,
                                        coordenadas[1] + (coordenadas[3] - coordenadas[1]) / 2,
                                        text=str(nodo.get_data()))

                # Dibujamos los nodos izquierdos
                self.dibujar_arbol(nodo.left, coordenadas_nodo_izquierdo, separacion + 60)

                # Dibujamos los nodos derechos
                self.dibujar_arbol(nodo.right, coordenadas_nodo_derecho, separacion + 60)

        # Datos necesarios
        # Profundidad del árbol
        # Nodos en un nivel determinado
        # Lista de nodos

    def set_arbol(self, arbol: BinaryTree):
        self.arbol = arbol

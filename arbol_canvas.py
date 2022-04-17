from tkinter import *
from estructuras.binary_tree import BinaryTree
import uuid


class Arbol(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Elementos del frame
        self.config(width=1000, height=350, bg="#146356")

        self.matriz_frames = []
        self.coordenadas = {}

        self.filas = 9
        self.columnas = 17

        self.arbol = BinaryTree(5)

    def dibujar_matriz(self):
        # Definimos la cantidad de filas que tendrá el frame
        for i in range(self.filas):
            self.rowconfigure(i, weight=1)

        # Definimos la cantidad de columnas que tendrá el frame
        for i in range(self.columnas):
            self.columnconfigure(i, weight=1)

        for i in range(self.filas):
            sub_matriz = []
            for j in range(self.columnas):
                nodo_frame = Frame(self, width=40, height=40, bg='#141E27',
                                   highlightbackground="black", highlightthickness=1)
                nodo_frame.pack_propagate(False)
                sub_matriz.append(nodo_frame)

                # Posicionamos el frame
                nodo_frame.grid(row=i, column=j)

            self.matriz_frames.append(sub_matriz)

    def dibujar_arbol(self):

        self.dibujar_matriz()

        # Agregamos nodos ficticios
        self.arbol.insert_left(3, 5)
        self.arbol.insert_right(7, 5)

        # 7
        self.arbol.insert_left(2, 7)
        self.arbol.insert_right(6, 7)

        self.arbol.complete_tree()

        contador = 2

        for nivel in range(self.arbol.max_depth()):
            
            nodos_nivel = self.arbol.level_nodes(nivel)

            if nivel == 0:
                self.insertar_raiz(nivel, nodos_nivel)

            if nivel >= 1:
                # Para los primeros hijos
                self.insertar_nodos(nivel + contador, nivel + contador, nodos_nivel)
                contador += 1

    # Función para insertar el nodo raíz
    def insertar_raiz(self, profundidad_y: int, nodo):
        punto_medio_x = int(round(self.columnas / 2))
        
        nodo_raiz = self.matriz_frames[profundidad_y][punto_medio_x]

        # Datos del nodo
        nodo_dato = nodo[0].get_data()
        id_nodo = hex(id(nodo[0]))

        # Pintamos el nodo raíz
        nodo_raiz.config(bg='#FFC107')

        # Ponemos el dato del nodo raíz
        Label(nodo_raiz, text=nodo_dato, bg='#FFC107').pack()
        Label(nodo_raiz, text=id_nodo, bg='#FFC107', font=("Helvetica", 7)).pack()

        # Ponemos las flechas


    # Función para insertar nodos
    def insertar_nodos(self, profundidad_y: int, separacion_x: int, nodos: list):
        punto_medio = int(round(self.columnas / 2))

        print("Nodos: ", nodos)

        # Por la cantidad de nodos que tiene el nivel
        for i in range(0, len(nodos) + 1, 4):
            
            # Nodo derecho
            # Comprobamos que el nodo derecho exista
            if nodos[-1].get_data() is not None:
                nodo_derecho_frame = self.matriz_frames[profundidad_y][punto_medio + separacion_x - i]
                nodo_derecho_frame.config(bg='#FFC107')


                # Datos del nodo
                nodo_dato = nodos[-1].get_data()
                id_nodo = hex(id(nodos[-1]))

                # Label que contiene el dato del nodo
                Label(nodo_derecho_frame, text=nodo_dato, bg='#FFC107').pack()

                # Label que contiene el id del nodo
                Label(nodo_derecho_frame, text=id_nodo, bg='#FFC107', font=("Helvetica", 7)).pack()
            
            # Nodo izquierdo
            # Comprobamos que el nodo izquierdo exista
            if nodos[0].get_data() is not None:
                nodo_izquierdo_frame = self.matriz_frames[profundidad_y][punto_medio - separacion_x + i]
                nodo_izquierdo_frame.config(bg='#FFC107')

                # Datos del nodo
                nodo_dato = nodos[0].get_data()
                id_nodo = hex(id(nodos[0]))

                # Label que contiene el dato del nodo
                Label(nodo_izquierdo_frame, text=nodo_dato, bg='#FFC107').pack()
                Label(nodo_izquierdo_frame, text=id_nodo, bg='#FFC107', font=("Helvetica", 7)).pack()

            # Eliminamos los nodos
            nodos.pop()
            nodos.pop(0)


root = Tk()
arbol = Arbol(root)
arbol.dibujar_arbol()
arbol.pack()
root.mainloop()

from tkinter import *
from estructuras.binary_tree import BinaryTree
import uuid


class Arbol(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Elementos del frame
        self.config(width=1000, height=350, bg="#146356")

        self.matriz_nodos_frames = []
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

            self.matriz_nodos_frames.append(sub_matriz)

    def dibujar_arbol(self):

        self.dibujar_matriz()

        # Agregamos nodos ficticios
        self.arbol.insert_left(3, 5)
        self.arbol.insert_right(7, 5)

        # 3
        self.arbol.insert_left(2, 3)
        self.arbol.insert_right(6, 3)

        # 7

        self.arbol.complete_tree()

        matriz_arbol = self.arbol.to_list()

        matriz_arbol_hashes = []

        # Hacemos una copia del matriz arbol
        for fila in matriz_arbol:
            sub_matriz = []
            for nodo in fila:
                sub_matriz.append(nodo)
            
            matriz_arbol_hashes.append(sub_matriz)

        #
        # [[5], [2, 5], [8, 9, 22, 44], [11, 12, 14, 54, 23, 43, 98, 22]]
        #

        # Recorremos la matriz del árbol para insertar los nodos
        for i in range(len(matriz_arbol)):
            for j in range(len(matriz_arbol[i])):

                # Si el nodo es la raíz
                if i == 0 and j == 0:
                    id = uuid.uuid4()

                    self.insertar_raiz([i, round(self.columnas / 2)], matriz_arbol[i][j], id)
                    matriz_arbol_hashes[i][j] = id

                    break

                # Nodos hijos de la raíz
                elif len(matriz_arbol[i - 1]) == 1 and j == 0:

                    # Id para identificar cada nodo
                    id_izq = uuid.uuid4()
                    id_der = uuid.uuid4()

                    hash_nodo_padre = matriz_arbol_hashes[i - 1][0]
                    inf_nodo = self.coordenadas[hash_nodo_padre]

                    x, y = inf_nodo['coordenadas']

                    self.insertar_izquierda([x + 1, y - 1], matriz_arbol[i][j], id_izq)
                    self.insertar_derecha([x + 1, y + 1], matriz_arbol[i][j + 1], id_der)

                    # Guardamos los hashes de los nodos
                    matriz_arbol_hashes[i][j] = id_izq
                    matriz_arbol_hashes[i][j + 1] = id_der
                    break
                
                
                # Nodos hijos de los nodos hijos de la raíz
                contador = 0
                for z in range(int(len(matriz_arbol[i]) / 2)):

                    hash_nodo_padre = matriz_arbol_hashes[i - 1][z]
                    inf_nodo = self.coordenadas[hash_nodo_padre]

                    x, y = inf_nodo['coordenadas']

                    # Id para identificar cada nodo
                    id_izq = uuid.uuid4()
                    id_der = uuid.uuid4()

                    self.insertar_izquierda([x, y], matriz_arbol[i][contador + z], id_izq)
                    self.insertar_derecha([x, y], matriz_arbol[i][contador+z + 1], id_der)

                    # Guardamos los hashes de los nodos
                    matriz_arbol_hashes[i][contador+z] = id_izq
                    matriz_arbol_hashes[i][contador+z + 1] = id_der

                    contador += 1

                break

    # Función para insertar un nodo a la izquierda
    def insertar_raiz(self, coordenadas: list, valor: str, id):

        x, y = coordenadas

        frame_buscado = self.matriz_nodos_frames[x][y]
        
        # Pintamos de amarillo el nodo que se encuentre en esas coordenadas, además de agregarle
        # el texto que se le pase como parámetro
        frame_buscado.config(bg='#FFC300')
        Label(frame_buscado, text=valor, bg='#FFC300', font=("Helvetica", 12)).pack()

        self.coordenadas[id] = {'valor': valor, 'coordenadas': [x, y]}

    # Función para insertar un nodo a la derecha recibiendo las coordenadas de su padre
    def insertar_derecha(self, coordenadas: list, valor, id):
        x, y = coordenadas

        frame_buscado = self.matriz_nodos_frames[x + 2][y + 2]

        # Pintamos de amarillo el nodo que se encuentre en esas coordenadas, además de agregarle
        # el texto que se le pase como parámetro
        frame_buscado.config(bg='#FFC300')
        Label(frame_buscado, text=valor, bg='#FFC300', font=("Helvetica", 12)).pack()

        self.coordenadas[id] = {'valor': valor, 'coordenadas': [x + 2, y + 2]}

    # Función para insertar un nodo a la izquierda recibiendo las coordenadas de su padre
    def insertar_izquierda(self, coordenadas: list, valor, id):
        x, y = coordenadas

        frame_buscado = self.matriz_nodos_frames[x + 2][y - 2]

        # Pintamos de amarillo el nodo que se encuentre en esas coordenadas, además de agregarle
        # el texto que se le pase como parámetro
        frame_buscado.config(bg='#FFC300')
        Label(frame_buscado, text=valor, bg='#FFC300', font=("Helvetica", 12)).pack()

        self.coordenadas[id] = {'valor': valor, 'coordenadas': [x + 2, y - 2]}


root = Tk()
arbol = Arbol(root)
arbol.dibujar_arbol()
arbol.pack()
root.mainloop()

from tkinter import *
from estructuras.binary_tree import BinaryTree
from nodo_coordenada import NodoCoordenada


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
                nodo_frame = Frame(self, width=25, height=25, bg='#141E27',
                                   highlightbackground="black", highlightthickness=1)
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
        matriz_arbol_referencias = []

        lista_nodos = []

        # Recorremos la matriz del árbol y agregamos los nodos
        for filas in matriz_arbol:
            fila_referencias = []
            for elemento in filas:
                nodo = NodoCoordenada(elemento)
                fila_referencias.append(nodo)

            matriz_arbol_referencias.append(fila_referencias)

        #
        # [[5], [2, 5], [8, 9, 22, 44], [11, 12, 14, 54, 23, 43, 98, 22]]
        #

        # Recorremos la matriz del árbol para insertar los nodos
        for i in range(len(matriz_arbol)):
            for j in range(len(matriz_arbol[i])):

                # Si el nodo es la raíz
                if i == 0 and j == 0:
                    self.insertar_raiz([i, round(self.columnas / 2)], matriz_arbol[i][j])

                    break

                # Nodos hijos de la raíz
                elif len(matriz_arbol[i - 1]) == 1 and j == 0:
                    valor_anterior = matriz_arbol[i - 1][0]

                    x, y = self.coordenadas[valor_anterior]

                    self.insertar_izquierda([x + 1, y - 1], matriz_arbol[i][j])
                    self.insertar_derecha(
                        [x + 1, y + 1], matriz_arbol[i][j + 1])

                    print("Nodo padre: ", valor_anterior)
                    print("Nodo izquierdo: ", matriz_arbol[i][j])
                    print("Nodo derecho: ", matriz_arbol[i][j + 1])
                    print("Coor izquierdo: ", self.coordenadas)
                    print()

                    break

                # Nodos hijos de los nodos hijos de la raíz
                contador = 0
                for x in range(int(len(matriz_arbol[i]) / 2)):
                    nodo_padre = matriz_arbol[i - 1][x]

                    print("Nodo padre: ", nodo_padre)
                    print("Nodo hijo derecho: ",
                          matriz_arbol[i][contador+x + 1])
                    print("Nodo hijo izquierdo: ",
                          matriz_arbol[i][contador + x])

                    self.insertar_izquierda(
                        self.coordenadas[nodo_padre], matriz_arbol[i][contador + x])
                    self.insertar_derecha(
                        self.coordenadas[nodo_padre], matriz_arbol[i][contador+x + 1])

                    print("Coordenadas de hijos: ", self.coordenadas)
                    print()

                    contador += 1

                break

        print("Coordenadas: ", self.coordenadas)
        print("Matriz del árbol: ", matriz_arbol)
        print("Matriz del árbol referencias: ", matriz_arbol_referencias)

    # Función para insertar un nodo a la izquierda
    def insertar_raiz(self, coordenadas: list, valor):

        x, y = coordenadas
        self.matriz_nodos_frames[x][y].config(bg='#FFC300')

        self.coordenadas[valor] = [x, y]

    # Función para insertar un nodo a la derecha recibiendo las coordenadas de su padre
    def insertar_derecha(self, coordenadas: list, valor):
        x, y = coordenadas
        self.matriz_nodos_frames[x + 2][y + 2].config(bg='#FFC300')

        self.coordenadas[valor] = [x + 2, y + 2]

    # Función para insertar un nodo a la izquierda recibiendo las coordenadas de su padre
    def insertar_izquierda(self, coordenadas: list, valor):
        x, y = coordenadas
        self.matriz_nodos_frames[x + 2][y - 2].config(bg='#FFC300')

        self.coordenadas[valor] = [x + 2, y - 2]


root = Tk()
arbol = Arbol(root)
arbol.dibujar_arbol()
arbol.pack()
root.mainloop()

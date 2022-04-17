from tkinter import *
from estructuras.binary_tree import BinaryTree
from PIL import ImageTk, Image


class Arbol(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Elementos del frame
        self.config(width=1000, height=350, bg="#146356")

        self.matriz_frames = []
        self.coordenadas = {}

        self.filas = 9
        self.columnas = 17

        # Imagenes de las flechas
        self.diagonal_derecha = ImageTk.PhotoImage(Image.open("recursos/derecha.png").resize((40, 40)))
        self.diagonal_izquierda = ImageTk.PhotoImage(Image.open("recursos/izquierda.png").resize((40, 40)))

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
                self.dibujar_raiz(nivel, nodos_nivel)

            if nivel >= 1:
                # Para los primeros hijos
                self.dibujar_nivel(nivel + contador, nivel + contador, nodos_nivel)
                contador += 1
            
    # Función para insertar el nodo raíz
    def dibujar_raiz(self, profundidad_y: int, nodo):
        
        punto_medio_x = int(round(self.columnas / 2))
        self.dibujar_nodo(nodo[0], profundidad_y, 0)

        # Pintamos 2 flechas en la diagonal derecha e izquierda
        for i in range(1, 3):
            diagonal_izquierda = self.matriz_frames[profundidad_y + i][punto_medio_x - i]
            diagonal_derecha = self.matriz_frames[profundidad_y + i][punto_medio_x + i]

            Label(diagonal_izquierda, image=self.diagonal_izquierda, bg="#141E27").pack()
            Label(diagonal_derecha, image=self.diagonal_derecha, bg="#141E27").pack()

    # Función para insertar nodos
    def dibujar_nivel(self, profundidad_y: int, separacion_x: int, nodos: list):
        print("Nodos: ", nodos)

        # Por la cantidad de nodos que tiene el nivel
        for i in range(0, len(nodos) + 1, 4):

            # Obtenemos el nodo izquierdo y derecho
            nodo_izquierdo = nodos[0]
            nodo_derecho = nodos[-1]

            if nodo_izquierdo.get_data() is not None:
                self.dibujar_nodo(nodo_izquierdo, profundidad_y, -separacion_x + i)
                

            if nodo_derecho.get_data() is not None:
                self.dibujar_nodo(nodo_derecho, profundidad_y, separacion_x - i)
            
            # Eliminamos los nodos
            nodos.pop()
            nodos.pop(0)
    
    # Función para insertar UN NODO en la matriz
    def dibujar_nodo(self, nodo, profundidad_y, separacion_x):
        punto_medio = int(round(self.columnas / 2))
        frame_buscado = self.matriz_frames[profundidad_y][punto_medio + separacion_x]

        # Cambiamos de color al frame
        frame_buscado.config(bg='#FFC107')

        # Datos del nodo
        nodo_dato = nodo.get_data()
        id_nodo = hex(id(nodo))

        # Label que contiene el dato del nodo
        Label(frame_buscado, text=nodo_dato, bg='#FFC107').pack()
        Label(frame_buscado, text=id_nodo, bg='#FFC107', font=("Helvetica", 7)).pack()


    def dibujar_flecha_derecha(self, coordenada_x: int, coordenada_y: int):
        frame_buscado = self.matriz_frames[coordenada_y + 1][coordenada_x + 1]
        Label(frame_buscado, image=self.diagonal_derecha, bg="#141E27").pack()

    def dibujar_flecha_izquierda(self, coordenada_x: int, coordenada_y: int):
        frame_buscado = self.matriz_frames[coordenada_y + 1][coordenada_x - 1]
        Label(frame_buscado, image=self.diagonal_izquierda, bg="#141E27").pack()
        

root = Tk()
arbol = Arbol(root)
arbol.dibujar_arbol()
arbol.pack()
root.mainloop()

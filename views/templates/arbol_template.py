from tkinter import *
from PIL import ImageTk, Image
from models.binary_tree_models import InformacionArbolBinario


class ArbolInterfaz(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Elementos del frame
        self.config(width=1000, height=350)

        self.matriz_frames = []
        self.coordenadas = {}

        self.filas = 9
        self.columnas = 17

        # Imagenes de las flechas
        self.diagonal_derecha = ImageTk.PhotoImage(Image.open("resources/images/derecha.png").resize((40, 40)))
        self.diagonal_izquierda = ImageTk.PhotoImage(Image.open("resources/images/izquierda.png").resize((40, 40)))

        self.recta_derecha = ImageTk.PhotoImage(Image.open("resources/images/recta_derecha.png").resize((40, 40)))
        self.recta_izquierda = ImageTk.PhotoImage(Image.open("resources/images/recta_izquierda.png").resize((40, 40)))

        self.inicializar_arbol()
    
    def actualizar(self, informacion_arbol):
        self.dibujar_arbol(informacion_arbol)

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
                nodo_frame = Frame(self, width=40, height=40, bg='white',
                                   highlightbackground="black")
                nodo_frame.pack_propagate(False)
                sub_matriz.append(nodo_frame)

                # Posicionamos el frame
                nodo_frame.grid(row=i, column=j)

            self.matriz_frames.append(sub_matriz)

    def dibujar_arbol(self, informacion_arbol: InformacionArbolBinario):
        
        self.destruir_frames()
        self.dibujar_matriz()

        contador = 2

        nodo_buscado = informacion_arbol.get_seleccionado()

        # Datos necesarios
        # Profundidad del árbol
        # Nodos en un nivel determinado
        # Lista de nodos

        for nivel in range(informacion_arbol.get_profundidad()):
            
            nodos_nivel = informacion_arbol.get_nodos_nivel()[nivel]
            profundidad_y = nivel + contador

            if nivel == 0:
                self.dibujar_raiz(nivel, nodos_nivel)

            if nivel >= 1:
                # Para los primeros hijos
                self.dibujar_nivel(profundidad_y, profundidad_y, nodos_nivel, nodo_buscado)
                contador += 1
            
    # Función para insertar el nodo raíz
    def dibujar_raiz(self, profundidad_y: int, nodo):
        
        punto_medio_x = int(round(self.columnas / 2))
        self.dibujar_nodo(nodo[0], profundidad_y, punto_medio_x)

        # Pintamos 2 flechas en la diagonal izquierda
        self.dibujar_flecha_izquierda(profundidad_y, punto_medio_x, self.recta_izquierda)
        self.dibujar_flecha_izquierda(profundidad_y + 1, punto_medio_x - 1)

        # Pintamos 2 flechas en la diagonal derecha
        self.dibujar_flecha_derecha(profundidad_y, punto_medio_x, self.recta_derecha)
        self.dibujar_flecha_derecha(profundidad_y + 1, punto_medio_x + 1)

    # Función para insertar nodos
    def dibujar_nivel(self, profundidad_y: int, separacion_x: int, nodos: list, valor_buscado=None):
        punto_medio = int(round(self.columnas / 2))

        # Por la cantidad de nodos que tiene el nivel
        encontrado = False
        for i in range(0, len(nodos), 2):

            auxiliar = i * 2

            # Obtenemos el nodo izquierdo y derecho
            nodo_izquierdo = nodos[0]
            nodo_derecho = nodos[-1]

            sep_izquierdo = punto_medio - separacion_x + auxiliar
            sep_derecho = punto_medio + separacion_x - auxiliar

            # Si este nodo no fue uno de relleno
            if nodo_izquierdo.get_data() is not None:

                # Comprobamos si el nodo izquierdo es el nodo buscado
                if nodo_izquierdo.get_data() == valor_buscado and not encontrado:
                    self.dibujar_nodo(nodo_izquierdo, profundidad_y, sep_izquierdo, '#54BAB9')

                    encontrado = True

                elif not nodo_izquierdo == valor_buscado:
                    self.dibujar_nodo(nodo_izquierdo, profundidad_y, sep_izquierdo)

                # Comprobamos que el nodo tenga algún hijo
                if not nodo_izquierdo.is_leaf():

                    # Comprobamos que el nodo izquierdo tenga hijos
                    if nodo_izquierdo.have_left_child():
                        self.dibujar_flecha_izquierda(profundidad_y, sep_izquierdo)
                    
                    # Comprobamos que el nodo derecho tenga hijos
                    if nodo_izquierdo.have_right_child():
                        self.dibujar_flecha_derecha(profundidad_y, sep_izquierdo)

            if nodo_derecho.get_data() is not None:

                # Comprobamos si el nodo es el que estamos buscando
                if nodo_derecho.get_data() == valor_buscado and not encontrado:
                    self.dibujar_nodo(nodo_derecho, profundidad_y, sep_derecho, '#54BAB9')

                    encontrado = True
                
                elif not nodo_derecho.get_data() == valor_buscado:
                    self.dibujar_nodo(nodo_derecho, profundidad_y, sep_derecho)

                # Si este nodo no tiene ningún hijo
                if not nodo_derecho.is_leaf():

                    # Comprobamos si tiene un hijo derecho
                    if nodo_derecho.have_right_child():
                        self.dibujar_flecha_derecha(profundidad_y, sep_derecho)
    
                    # Comprobamos si tiene un hijo izquierdo
                    if nodo_derecho.have_left_child():
                        self.dibujar_flecha_izquierda(profundidad_y, sep_derecho)

            # Eliminamos los nodos
            nodos.pop()
            nodos.pop(0)
    
    # Función para insertar UN NODO en la matriz
    def dibujar_nodo(self, nodo, coordenada_y, coordenada_x, color='#FFD93D'):
        frame_buscado = self.matriz_frames[coordenada_y][coordenada_x]

        # Cambiamos de color al frame
        frame_buscado.config(bg=color)

        # Datos del nodo
        nodo_dato = nodo.get_data()
        id_nodo = nodo.get_id()

        # Label que contiene el dato del nodo
        Label(frame_buscado, text=nodo_dato, bg=color).pack()
        Label(frame_buscado, text=id_nodo, bg=color, font=("Helvetica", 7)).pack()

    def dibujar_flecha_derecha(self, coordenada_y: int, coordenada_x: int, imagen=None):
        frame_buscado = self.matriz_frames[coordenada_y + 1][coordenada_x + 1]
        flecha = Label(frame_buscado, image=self.diagonal_derecha, bg="white")

        if imagen is not None:
            flecha.config(image=imagen)
        
        flecha.pack()

    def dibujar_flecha_izquierda(self, coordenada_y: int, coordenada_x: int, imagen=None):
        frame_buscado = self.matriz_frames[coordenada_y + 1][coordenada_x - 1]
        flecha = Label(frame_buscado, image=self.diagonal_izquierda, bg="white")

        if imagen is not None:
            flecha.config(image=imagen)
        
        flecha.pack()

    def inicializar_arbol(self):
        self.dibujar_matriz()
    
    def destruir_frames(self):
        # Recorremos todos los frames y les ponemos el fondo blanco
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                self.matriz_frames[i][j].destroy()
        
        self.matriz_frames.clear()
from estructuras.binary_tree import BinaryTree
from tkinter import Tk
from arbol_canvas import ArbolInterfaz

root = Tk()
arbol = BinaryTree(5)
arbol.insert_left(3, 5)
arbol.insert_right(2, 5)

arbol.insert_right(4, 3)
arbol.insert_left(1, 3)

arbol.insert_right(6, 2)
arbol.insert_left(7, 2)

arbol.insert_right(8, 6)
arbol.insert_left(9, 6)

arbol.insert_left(12, 7)

arbol.insert_left(19, 1)
arbol.insert_right(20, 1)

arbol_can = ArbolInterfaz(root)

arbol_can.set_arbol(arbol)

arbol_can.dibujar_arbol()
arbol_can.pack()

root.mainloop()

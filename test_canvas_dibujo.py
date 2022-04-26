from arbol_canvas import ArbolInterfaz
from tkinter import Tk

root = Tk()

arbol_can = ArbolInterfaz(root)
arbol_can.test_dibujo()
arbol_can.pack()

root.mainloop()

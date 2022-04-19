from tkinter import *


class BotonesArbol(Frame):
    def __init__(self, master, manager):
        Frame.__init__(self, master)

        self.manager = manager

        # Elementos del frame
        self.dato_label = Label(self, text="Valor: ")
        self.dato_entry = Entry(self)

        self.eliminar = Button(self, text="Eliminar", command=self.eliminar)
        self.buscar = Button(self, text="Buscar", command=self.buscar)

        self.insertar_raiz = Button(self, text="Insertar raiz", command=self.insertar_raiz)
    
    def eliminar(self):
        self.manager.get_estructura().remove_node(self.dato_entry.get())
        self.manager.actualizar()
        
    def buscar(self):
        self.manager.get_estructura().search(self.dato_entry.get())
        self.manager.actualizar()

    def insertar_raiz(self):
        self.manager.get_estructura().insert_root(self.dato_entry.get()).set_buscado(True)
        self.manager.actualizar()

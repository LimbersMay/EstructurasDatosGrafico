from tkinter import *

# Clase plantilla para los botones inferiores de todas los tipos de listas
class PlantillaBotones(Frame):

    def __init__(self, master, lista_interfaz):
        Frame.__init__(self, master)

        # Atributos
        self.lista_interfaz = lista_interfaz
        
        # Elementos del frame
        self.dato_label = Label(self, text="Valor: ")
        self.dato_entry = Entry(self)

        self.insertar_final = Button(self, text="Insertar al final", command=self.insertar_final)
        self.insertar_inicio = Button(self, text="Insertar al inicio", command=self.insertar_inicio)

        self.eliminar_final = Button(self, text="Eliminar al final", command=self.eliminar_final)
        self.eliminar_inicio = Button(self, text="Eliminar al inicio", command=self.eliminar_inicio)

        self.buscar_button = Button(self, text="Buscar")
    
    def insertar_final(self):
        self.lista_interfaz.insertar_final(self.dato_entry.get())
    
    def insertar_inicio(self):
        self.lista_interfaz.insertar_inicio(self.dato_entry.get())

    def eliminar_final(self):
        self.lista_interfaz.eliminar_final()
    
    def eliminar_inicio(self):
        self.lista_interfaz.eliminar_inicio()
    
    def buscar(self):
        self.lista_interfaz.buscar(self.dato_entry.get())
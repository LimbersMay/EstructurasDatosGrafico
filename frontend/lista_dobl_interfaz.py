from tkinter import *
from estructuras.lista_dob_enlazada.double_linked_list import DoubleLinkedList
from frontend.lista_interfaz import ListaInterfaz

class ListaDobEnlazadaInterfaz(ListaInterfaz):
    
    def __init__(self, master):
        super().__init__(master)
        
        self.lista = DoubleLinkedList()
    
    def dibujar_lista(self):
        super().dibujar_lista()

    # Métodos de la lista enlazada doble
    def insertar_inicio(self, data):
        super().insertar_inicio(data)
    
    def insertar_final(self, data):
        super().insertar_final(data)
    
    def insertar_posicion(self, data, posicion):
        self.lista.append_in_position(data, posicion)

        super().dibujar_lista()
    
    def eliminar_inicio(self):
        super().eliminar_inicio()
    
    def eliminar_final(self):
        super().eliminar_final()
    
    def eliminar_por_posicion(self, posicion):
        self.lista.remove_node_position(posicion)
    
    def buscar(self, valor):
        super().dibujar_lista(valor)
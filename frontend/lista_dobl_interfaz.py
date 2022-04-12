from tkinter import *
from estructuras.lista_dob_enlazada.double_linked_list import DoubleLinkedList
from lista_interfaz import ListaInterfaz

class ListaDobEnlazadaInterfaz(ListaInterfaz, Frame):
    
    def __init__(self, master):
        ListaInterfaz.__init__(self, master)
        Frame.__init__(self, master)
        
        self.lista = DoubleLinkedList()
        self.lista_frames = []
        
        # Configuraciones de la ventana
        self.config(width=800, height=350, bg="#146356")
        self.grid_propagate(False)
        
        self.rowconfigure(0, weight=1)
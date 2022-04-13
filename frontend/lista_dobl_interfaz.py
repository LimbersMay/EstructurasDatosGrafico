from estructuras.double_linked_list import DoubleLinkedList
from frontend.lista_simple_template import ListaInterfaz

class ListaDobEnlazadaInterfaz(ListaInterfaz):
    
    def __init__(self, master):
        super().__init__(master)
        
        self.lista = DoubleLinkedList()
    
    def insertar_posicion(self, data, posicion):
        self.lista.append_in_position(data, posicion)

        self.dibujar_lista()
    
    def eliminar_por_posicion(self, posicion):
        self.lista.remove_node_position(posicion)

        self.dibujar_lista()
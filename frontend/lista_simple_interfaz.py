from estructuras.linked_list import LinkedList
from frontend.lista_simple_template import ListaInterfaz


class ListaSimpleInterfaz(ListaInterfaz):
    def __init__(self, master):
        super().__init__(master)

        self.lista = LinkedList()

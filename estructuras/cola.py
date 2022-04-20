from lib2to3.pytree import Node
from .node_information import NodeInformation
from .lineal_structure_information import LinealStructureInformation

class Nodo:
    def __init__(self, elemento):
        self.data = elemento
        self.siguiente = None
        # Variable para saber si estamos buscando este nodo
        self.buscado = False

    def __str__(self):
        return f"{self.data}"

    def set_buscado(self, buscado):
        self.buscado = buscado


class Cola:
    def __init__(self, max=-1):
        self._size = 0
        self.frente = None
        self.fondo = None
        self.max = max

    def enqueue(self, elemento):
        # 1. - construir el nodo
        nuevo = Nodo(elemento)

        # 2 - visitar el nodo
        # 3 - consultar si la cola esta vacia
        if self.frente == None and self.fondo == None:
            # 3.1  Frente y fondo apuntan a nuevo
            self.frente = nuevo
            self.fondo = nuevo

        elif self._size == self.max:
            raise Exception('No hay espacio, DESBORDAMIENTO DE PILA')

        else:
            self.fondo.siguiente = nuevo
            self.fondo = nuevo
            # 4 - actualizar datos
        self._size += 1

    def recorrer(self):
        resultado = ''
        aux = self.frente
        while aux is not None:
            # 2 - visitar el nodo
            resultado = resultado + str(aux) + '\n'
            # 3- mover el auxiliar
            aux = aux.siguiente

        return resultado

    def search(self, elemento) -> NodeInformation:
        aux = self.frente
        vistos = 0
        while vistos < self._size:
            if elemento == aux.data:
                return aux.data
            else:
                aux = aux.siguiente
            vistos += 1

        if vistos == self._size:
            raise Exception('Error, el elemento no existe')

    # Method that return the node in an index
    def search_position_node(self, index):
        if index < 0 or index >= self._size:
            raise Exception('Index out of range')
        aux = self.frente
        for i in range(index):
            aux = aux.siguiente
        return aux

    def dequeue(self):
        # 1- crear el auxiliar (señalar al frente)
        aux = self.frente

        if self._size == 0:
            raise Exception('SUBDESBORDAMIENTO DE COLA')
        elif self._size == 1:
            self.frente = None
            self.fondo = None
        else:
            # 2- Mover al frente al siguiente elemento 
            self.frente = aux.siguiente

            # 3- quitar enlaces
            aux.siguiente = None

        # 4- disminuir tamaño
        self._size -= 1

        # 5- devolver el nodo eliminado
        return aux

    def __str__(self):
        return f"Tamaño: {self._size}\nMax: {self.max}\nFrente: {self.frente}\nFondo: {self.fondo}"

    def get_size(self):
        return self._size

    def get_max(self):
        return self.max

    def get_head(self):
        return self.frente.data

    def get_tail(self):
        return self.fondo.data

    def get_nodes_information(self):
        nodes_information = []

        for i in range(self._size):
            actual_node = self.search_position_node(i)
            nodes_information.append(NodeInformation(actual_node.data, id(actual_node)))

        return nodes_information

    def get_queue_information(self):
        queue_information = LinealStructureInformation(self.get_head(), self.get_tail(), self.get_size(),
                                                       self.get_max())

        return queue_information

from typing import Optional, TypeVar, Generic
from node import Node

T = TypeVar('T')


# Crea una lista que solo permita nodos de un tipo de dato (genérico)
class LinkedList(Generic[T]):
    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0

    # Método que utiliza la función len() de python para determinar el número de elementos en la estructura
    def __len__(self) -> int:
        return self._size

    # Atributo de lectura para acceder a la data del primer nodo
    # Si no hay elementos lanza una excepción
    @property
    def first(self) -> T:
        if self.is_empty():
            raise Exception('Linked List is empty')
        else:
            return self._head.data

    # Atributo de lectura para acceder a la data del último nodo
    # Si no hay elementos lanza una excepción
    @property
    def last(self) -> T:
        if self.is_empty():
            raise Exception('Linked List is empty')
        else:
            return self._tail.data

    # Método que verifica si la lista enlazada se encuentra vacía (no hay nodos)
    def is_empty(self):
        return self._head is None and self._tail is None

    # Método para recorrer todos los nodos de una lista, devuelve una cadena con toda la data
    def traversal(self) -> str:
        result: str = ''
        current: Optional[Node] = self._head
        while current is not None:
            if current == self._tail:
                result += str(current)
            else:
                result += str(current) + '->'
            current = current.next
        return result

    # Método que busca el nodo que contenga un valor en específico
    # Devuelve la primera coincidencia
    # Si no hay nodos con ese valor, debe lanzar una excepción
    def search_node_positon(self, data):
        iterations = 0
        aux = self._head

        while aux is not None:
            if aux.data == data:
                return iterations

            else:
                iterations += 1
                aux = aux.next

        raise Exception('El elemento no existe')

    def search_position_node(self, position):
        iterations = 0
        aux = self._head

        while aux is not None:
            if position == iterations:
                return aux

            else:
                iterations += 1
                aux = aux.next

        raise Exception('Posicion inexistente')

    def search(self, data) -> Node:
        aux = self._head

        while aux is not None:
            if aux.data is data:
                return aux

            else:
                aux = aux.next

        raise Exception('Inexistent element')

    # Método que añade al inicio un nuevo nodo a la lista
    def prepend(self, data) -> None:
        new = Node(data)

        if self.is_empty():
            self._head = new
            self._tail = new

        else:
            self._tail.next = new
            self._tail = new

        self._size += 1

    # Método que añade al final un nuevo nodo a la lista
    def append(self, data: T) -> None:
        new_node: Node = Node(data)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    # Método que elimina el primer nodo que contenga el valor pasado como parámetro
    def remove_head(self):
        aux = self._head

        if self.is_empty():
            raise Exception('Subdesbordamiento')

        elif self._size == 1:
            self._head = None
            self._tail = None

        else:
            self._head = aux.next
            aux.next = None

        self._size -= 1
        return aux

    def remove_tail(self):
        aux = self._tail

        if self.is_empty():
            raise Exception('Subdesbordamiento de lista')

        elif self._size == 1:
            self._head = None
            self._tail = None

        else:
            slot = self.search_node_position(aux.nombre)
            precedent = self.search_position_node(slot - 1)

            precedent.next = None
            self._tail = precedent

        self._size -= 1
        return aux

    def remove(self, data) -> T:
        aux = self.search(data)

        if self._head == aux:
            self.remove_head()

        elif self._tail == aux:
            self.remove_tail()

        else:
            slot = self.search_node_position(data)
            anterior = self.search_position_node(slot - 1)

            anterior.next = aux.next
            aux.next = None

        self._size -= 1
        return aux

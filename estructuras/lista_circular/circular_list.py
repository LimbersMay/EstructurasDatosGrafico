from typing import Optional, TypeVar
from .node import Node


T = TypeVar('T')


class CircularList:
    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0
        
    def move_left(self) -> Node:
        if self.is_empty():
            raise Exception('Empty List')

        else:
            aux = self._head
            self._tail = self._head
            self._head = self._head.next

            return aux

    def move_right(self) -> Node:
        if self.is_empty():
            raise Exception('Empty List')

        else:
            aux = self._tail
            precedent = self._position_search(self._size - 2)
            self._head = self._tail
            self._tail = precedent

            return aux

    def remove_head(self) -> Node:
        if self.is_empty():
            raise Exception('Subdesbordamiento')

        elif self._head == self._tail:
            self._head = None
            self._tail = None
            self._tail.next = None

        else:
            aux = self._head
            self._head = self._head.next
            self._tail.next = self._head
            aux.next = None

        self._size -= 1
        return aux

    def remove_tail(self) -> Node:
        if self.is_empty():
            raise Exception('Subdesbordamiento')

        elif self._head == self._tail:
            self._head = None
            self._tail = None
            self._tail.next = None

        else:
            aux = self._tail
            precedent = self._position_search(self._size - 2)

            precedent.next = self._head
            self._tail.next = None
            self._tail = precedent

        self._size -= 1
        return aux

    def remove(self, data: T) -> Node:
        aux = self._search(data)

        if aux == self._head:
            self.remove_head()

        elif aux == self._tail:
            self.remove_tail()

        else:
            position = self._search_positon(aux.data)
            precedent = self._position_search(position-1)

            precedent.next = aux.next
            aux.next = None

            self._size -= 1
        return aux

    def _position_search(self, number: int) -> Node:
        aux = self._head
        iterations = 0

        while iterations <= self._size:
            if iterations is number:
                return aux

            else:
                aux = aux.next
                iterations += 1

        raise Exception('Invalid search')

    def _search_positon(self, data: T) -> int:
        aux = self._head
        iterations = 0

        while aux is not self._tail:
            if aux.data == data:
                return iterations

            else:
                aux = aux.next
                iterations += 1

        if aux.data == self._tail.data:
            return iterations

        else:
            raise Exception('Invalid search')

    def _search(self, data: T) -> Node:
        aux = self._head

        while aux is not self._tail:
            if aux.data == data:
                return aux

            else:
                aux = aux.next

        if aux.data == self._tail.data:
            return aux

        else:
            raise Exception('Invalid search')

    def is_empty(self) -> bool:
        return self._head is None and self._tail is None and self._size == 0

    def append(self, data) -> Node:
        new = Node(data)

        if self.is_empty():
            self._head = new
            self._tail = new
            self._tail.next = self._head

        else:
            new.next = self._head
            self._tail.next = new
            self._tail = new

        self._size += 1
        return new

    def prepend(self, data):
        if self.is_empty():
            new_node = Node(data)
            self._head = new_node
            self._tail = new_node
            self._tail.next = self._head
            self._size += 1
        else:
            new_node = Node(data)
            new_node.next = self._head
            self._head = new_node
            self._tail.next = self._head
            self._size += 1

    def traversal(self) -> str:
        result = ''
        aux = self._head
        while aux is not self._tail:
            result += str(aux.data) + ' -> '
            aux = aux.next
        result += str(self._tail.data)
        return result
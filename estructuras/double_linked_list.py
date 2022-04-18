from typing import Optional, TypeVar

T = TypeVar('T')

class Node:
    def __init__(self, data) -> None:
        self.prev: Optional[Node] = None
        self.data: T = data
        self.next: Optional[Node] = None

    def __str__(self):
        return self.data


class DoubleLinkedList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    # Get items
    @property
    def head(self) -> Node:
        return self._head

    @property
    def tail(self) -> Node:
        return self._tail

    def __len__(self):
        return self._size

    # Insercion of items in the list
    def prepend(self, data: T) -> Node:
        new = Node(data)

        if self.is_empty():
            self._head = new
            self._tail = new

            self._head.next = self._tail
            self._tail.next = self._head

        else:
            new.next = self._head
            self._head.prev = new
            self._head = new

        self._size += 1
        return new

    def append(self, data: T) -> Node:
        new = Node(data)
        if self.is_empty():
            self._head = new
            self._tail = new

            self._head. next = self._tail
            self._tail.prev = self._head

        else:
            new.prev = self._tail
            self._tail.next = new
            self._tail = new

        self._size += 1
        return new

    def append_in_position(self, data: T, position: int) -> Node:
        new = Node(data)

        if self.is_empty():
            self._head = new
            self._tail = new

            self._head.next = self._tail
            self._tail.prev = self._head

        else:
            aux = self.position_search(position)

            if aux is self._head:
                self.prepend(data)

            elif aux is self._tail:
                self.append(data)

            else:
                new.next = aux.next
                new.prev = aux
                aux.next = new
                new.next.prev = new
                self._size += 1
                return new

    # Method that removes the head
    def remove_head(self) -> Node:
        if self.is_empty():
            raise Exception('subdesbordamiento')

        elif self._size == 1:
            self._head = None
            self._tail = None

        else:
            aux = self._head
            self._head = self._head.next
            self._head.prev = None

            self._size -= 1
            return aux

    def remove_tail(self) -> Node:
        if self.is_empty():
            raise Exception('subdesbordamiento')

        elif self._size == 1:
            self._head = None
            self._tail = None

            self._size -= 1

        else:
            prev_tail = self._tail
            self._tail = self._tail.prev
            prev_tail.prev = None

            self._size -= 1
            return prev_tail

    def remove(self, data: T) -> Node:
        aux = self.search(data)

        if aux == self._head:
            self.remove_head()

        elif aux == self._tail:
            self.remove_tail()

        else:
            position = self.get_position(data)
            prev = self.position_search(position-1)

            prev.next = aux.next
            aux.next.prev = prev
            aux.next = None
            aux.prev = None

            self._size -= 1
            return aux
    
    # Method that remove a node by position
    def remove_node_position(self, position: int) -> Node:
        aux = self.position_search(position)

        if aux is self._head:
            self.remove_head()

        elif aux is self._tail:
            self.remove_tail()

        else:
            prev = self.position_search(position-1)
            prev.next = aux.next
            aux.next.prev = prev
            aux.next = None
            aux.prev = None

            self._size -= 1
            return aux

    # Method that return the node in one position
    def search_position_node(self, position: int) -> Node:
        aux = self._head
        iterations = 0

        while iterations <= self._size:
            if iterations == position:
                return aux

            else:
                aux = aux.next
                iterations += 1

        raise Exception('Invalid position')

    def search_position(self, data: T) -> int:
        aux = self._head
        iterations = 0

        while aux is not self._tail:
            if aux.data == data:
                return iterations

            else:
                aux = aux.next
                iterations += 1

        if aux == self._tail:
            return iterations

        else:
            raise Exception('No item found')

    def position_search(self, position: int) -> Node:
        aux = self._head
        iterations = 0

        while iterations <= self._size:
            if iterations == position:
                return aux

            else:
                aux = aux.next
                iterations += 1

        raise Exception('Invalid position')

    def get_position(self, data: T) -> int:
        aux = self._head
        iterations = 0

        while aux is not self._tail:
            if aux.data == data:
                return iterations

            else:
                aux = aux.next
                iterations += 1

        if self._tail.data == data:
            return iterations

        else:
            raise Exception('Data not found')

    # Traverse list
    def traverse_forward(self) -> str:
        output = ''
        aux = self._head

        while aux is not self._tail:
            output += str(aux.data) + ' -> '
            aux = aux.next
            
        output += str(self._tail.data)
        return output

    def traverse_backwards(self) -> str:
        output = ''
        aux = self._tail

        while aux is not self._head:
            output += str(aux.data) + ' -> '
            aux = aux.prev

        output += str(self._head.data)
        return output

    # Other methods
    def is_empty(self) -> bool:
        return self._head is None and self._tail is None

    def get_head(self) -> Node:
        return self._head.data
    
    def get_tail(self) -> Node:
        return self._tail.data
    
    def get_size(self) -> int:
        return self._size
from typing import Optional, TypeVar


T = TypeVar('T')


class Node:
    def __init__(self, data):
        self.data: T = data
        self.next: Optional[Node] = None

    def __str__(self):
        return str(self.data)

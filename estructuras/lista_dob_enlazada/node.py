from typing import Optional, TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, data) -> None:
        self.prev: Optional[Node] = None
        self.data: T = data
        self.next: Optional[Node] = None

    def __str__(self):
        return self.data

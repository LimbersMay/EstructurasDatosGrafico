from typing import Optional, TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional[Node] = None

    def __str__(self) -> str:
        return str(self.data)

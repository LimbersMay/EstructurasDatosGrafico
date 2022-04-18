from __future__ import annotations
from typing import Optional, TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, data: T):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def is_leaf(self):
        return self.left is None and self.right is None
    
    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_data(self):
        return self.data


class BinarySearchTree:
    def __init__(self, data=None):
        self.__root = Node(data)

    def insert(self, data, *args):
        subtree = self.__root if len(args) == 0 else args[0]

        
        if subtree.data is None:
            subtree.data = data
            return

        if data < subtree.data and data:
            if subtree.left is None:
                subtree.left = Node(data)

            else:
                self.insert(data, subtree.left)

        elif data > subtree.data:
            if subtree.right is None:
                subtree.right = Node(data)

            else:
                self.insert(data, subtree.right)

    def pre_order(self, *args) -> str:
        node = self.__root if len(args) == 0 else args[0]

        if node is not None:
            if node.is_leaf():
                return str(node.data)

            else:
                result = str(node.data) + ' ('
                result += self.pre_order(node.left) + ', '
                result += self.pre_order(node.right) + ')'

                return result

        else:
            return ''

    def in_order(self, *args):
        node = self.__root if len(args) == 0 else args[0]
        if node is not None:
            if node.is_leaf():
                return str(node.data)

            else:
                result = '(' + self.in_order(node.left)
                result += str(node.data)
                result += self.in_order(node.right) + ')'

                return result

    # Method that insert the root of the tree
    def insert_root(self, data):
        if self.__root.get_data() is None:
            self.__root = Node(data)
    
    # Method that return the maximum depth of the tree
    def max_depth(self, *args) -> int:
        node = self.__root if len(args) == 0 else args[0]
        current_level = args[1] if len(args) >= 1 else 1

        if node is not None:
            if node.is_leaf():
                return current_level

            else:
                left = self.max_depth(node.left, current_level + 1)
                right = self.max_depth(node.right, current_level + 1)

                return max(left, right)

        else:
            return -1

    
    # Convert the binary tree to a list using Eytzi's algorithm
    def to_list(self) -> list:
        result = []

        def to_list(node: Node, level: int) -> None:
            if node is not None:
                if level == len(result):
                    result.append([])

                result[level].append(node.data)

                to_list(node.left, level + 1)
                to_list(node.right, level + 1)

        to_list(self.__root, 0)

        return result
    
    # Complete the binary tree puting all the missing nodes in the left side
    def complete_tree(self, *args) -> None:
        node = self.__root if len(args) == 0 else args[0]
        current_level = args[1] if len(args) >= 1 else 1
        
        if node is not None:
            if node.is_leaf() and current_level == self.max_depth():
                return

            else:
                if node.left is None:
                    node.left = Node(None)

                if node.right is None:
                    node.right = Node(None)

                self.complete_tree(node.left, current_level + 1)
                self.complete_tree(node.right, current_level + 1)

    # Method that returns the nodes of a level
    def level_nodes(self, level: int, values=False) -> list:
        result_references = []
        result_values = []

        def level_nodes(node: Node, level: int) -> None:
            if node is not None:
                if level == len(result_references):
                    result_references.append([])
                    result_values.append([])

                result_references[level].append(node)
                result_values[level].append(node.data)

                level_nodes(node.left, level + 1)
                level_nodes(node.right, level + 1)

        level_nodes(self.__root, 0)

        if values:
            return result_values[level]
        
        return result_references[level]
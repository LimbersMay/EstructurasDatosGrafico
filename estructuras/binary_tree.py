from __future__ import annotations
from typing import Optional, TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, data: T, father: Optional[Node] = None):
        self.data = data
        self.father = father
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

        self.visited = False

    def is_leaf(self):
        return self.left is None and self.right is None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_data(self):
        return self.data


class BinaryTree:
    def __init__(self, data=None):
        self.__root = Node(data)

    # Method that insert a node on the left side with a reference
    def insert_left(self, data: T, ref: T):
        node = self.__search(ref)

        if node is not None:
            new_node = Node(data, node)

            if node.left is None or node.left.get_data() is None:
                node.left = new_node

            else:
                raise Exception('Left side is not empty.')

        else:
            raise Exception('The reference does not exist.')

    def insert_right(self, data: T, ref: T):
        node = self.__search(ref)

        if node is not None:
            new_node = Node(data)

            if node.right is None or node.right.get_data() is None:
                node.right = new_node

            else:
                raise Exception('Right side is not empty.')

        else:
            raise Exception('The reference does not exist.')

    def __str__(self):
        return self.pre_order()

    def depth(self, ref: T, *args) -> int:
        node = self.__root if len(args) == 0 else args[0]

        if node is None:
            return -1

        elif node.data == ref:
            return 0

        else:
            left = self.depth(ref, node.left)
            right = self.depth(ref, node.right)

            # No existe en ningun lado
            if left == -1 and right == -1:
                return -1

            # Existe en algun lado
            else:
                return max(left, right) + 1

    def height(self, *args) -> int:
        node = self.__root if len(args) == 0 else args[0]

        if node is None:
            return -1

        elif node.left is None and node.right is None:
            return +1

        else:
            left = self.height(node.left)
            right = self.height(node.right)

            return max(left, right) + 1

    def __search(self, data: T, *args) -> Optional[Node]:
        node = self.__root if len(args) == 0 else args[0]

        if node is not None:
            if node.data == data:
                return node

            else:
                result = self.__search(data, node.left)

                if result is None:
                    result = self.__search(data, node.right)

                    return result

                else:
                    return result

        else:
            return None

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
            return 'a'

    def in_order(self, *args) -> str:
        node = self.__root if len(args) == 0 else args[0]

        if node is not None:
            if node.is_leaf():
                return str(node.data)

            else:
                result = self.pre_order(node.left) + ' '
                result += str(node.data) + ' '
                result += self.pre_order(node.right) + ' '

                return result

        else:
            return 'a'

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

    # Search the father of a node
    def search_father(self, *args, child: Node) -> Optional[Node]:
        node = self.__root if len(args) == 0 else args[0]

        if node is not None:
            if node.is_leaf():
                return node

            else:

                if node.left == child or node.right == child:
                    return node

                father_left = self.search_father(node.left, child=child)
                father_right = self.search_father(node.right, child=child)

                if father_left is not None and not type(father_left) == str:
                    return father_left

                elif father_right is not None and not type(father_right) == str:
                    return father_right

        else:
            return None

    def search(self, data: T) -> Optional[Node]:
        return self.__search(data)

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

    # Method that returns the nodes of a level
    def level_nodes(self, level: int, values=False, references=False) -> list:
        self.complete_tree()
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

        if references:
            return result_references[level]

    # Method that insert the root of the tree
    def insert_root(self, data: T) -> None:
        if self.__root is None or self.__root.get_data() is None:
            self.__root = Node(data)

        else:
            raise Exception('The root already exists')

    # Method that returns the min node in the side of a node of reference
    def min_node(self, ref: Node) -> Optional[Node]:
        if ref is None:
            return None

        if ref.left is None:
            return ref

        return self.min_node(ref.left)

    def get_root(self) -> Node:
        return self.__root.data

    def get_root_reference(self) -> Node:
        return self.__root

    # Method that returns the return the total number of nodes in the tree
    def count_nodes(self, ) -> int:

        matrix_nodes = self.to_list()
        list_nodes = [element for sublist in matrix_nodes for element in sublist if element is not None]

        return len(list_nodes)

    def insert_in_level(self, level, list_data):

        if self.__root.data is None:
            self.__root = Node(list_data.pop(0))
            return

        level_nodes = self.level_nodes(level - 1, references=True)

        for i in range(len(level_nodes)):

            if level_nodes[i].left is None:
                self.insert_left(list_data.pop(0), level_nodes[i].data)

            if level_nodes[i].right is None:
                self.insert_right(list_data.pop(0), level_nodes[i].data)

    # Method that clears the tree
    def clear(self) -> None:
        self.__root.data = None

    # Method that search a node taking a node as reference
    def search_node(self, node: Node, data: T) -> Optional[Node]:
        if node is not None:
            if node.data == data:
                return node

            else:
                return self.search_node(node.left, data) or self.search_node(node.right, data)

        else:
            return None

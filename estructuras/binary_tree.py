from __future__ import annotations
from ast import arg
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


class BinaryTree:
    def __init__(self, data=None):
        self.__root = Node(data)

    # Method that insert a node in the left side with a reference
    def insert_left(self, data: T, ref: T):
        node = self.__search(ref)

        if node is not None:
            new_node = Node(data)

            if node.left is None:
                node.left = new_node

            else:
                raise Exception('Left side is not empty.')

        else:
            raise Exception('The reference does not exist.')

    def insert_right(self, data: T, ref: T):
        node = self.__search(ref)

        if node is not None:
            new_node = Node(data)

            if node.right is None:
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
    def search_father(self, *args, child: Node) -> str:
        node = self.__root if len(args) == 0 else args[0]

        if node is not None:
            if node.is_leaf():
                return str(node.data)

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
            return 'a'

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
    
    # Method that insert the root of the tree
    def insert_root(self, data: T) -> None:
        if self.__root is None:
            self.__root = Node(data)

        else:
            raise Exception('The root already exists')
    
    # Method that remove a node from a full binary tree
    def remove_node(self, data: T) -> None:
        
        node = self.__search(data)

        # Remove if the node is the root
        if node == self.__root:
            self.__root = None

        # Remove if the node is a leaf
        elif node.is_leaf():
            father = self.search_father(child=node)

            if father.left == node:
                father.left = None

            else:
                father.right = None
        
        # Remove if the node has only one child
        elif node.left is None or node.right is None:
            father = self.search_father(child=node)

            if father.left == node:
                if node.left is None:
                    father.left = node.right

                else:
                    father.left = node.left

            else:
                if node.left is None:
                    father.right = node.right

                else:
                    father.right = node.left
        
        # Remove if the node has two children
        else:
            father = self.search_father(child=node)

            if father.left == node:
                father.left = node.left

            else:
                father.right = node.left

            node.left = None


    # Method that returns the minimum node of a tree
    def min_node(self, *args) -> Node:
        node = self.__root if len(args) == 0 else args[0]

        if node is not None:
            if node.left is None:
                return node

            else:
                return self.min_node(node.left)

        else:
            return None
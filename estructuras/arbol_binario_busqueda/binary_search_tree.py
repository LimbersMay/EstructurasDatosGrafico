from node import Node


class BinarySearchTree:
    def __init__(self, data):
        self.__root = Node(data)

    def insert(self, data, *args):
        subtree = self.__root if len(args) == 0 else args[0]

        if data < subtree.data:
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

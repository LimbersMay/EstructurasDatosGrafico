from requests import delete
from estructuras.binary_tree import BinaryTree

binary_tree = BinaryTree(1)

binary_tree.insert_left(2, 1)
binary_tree.insert_right(3, 1)

binary_tree.insert_left(4, 2)
binary_tree.insert_right(5, 2)

binary_tree.insert_left(6, 3)
binary_tree.insert_right(7, 3)

binary_tree.insert_right(11, 7)

print(binary_tree.pre_order())

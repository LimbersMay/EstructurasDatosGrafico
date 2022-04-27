from estructuras.binary_tree import BinaryTree

binary_tree = BinaryTree()

binary_tree.insert_root(5)

binary_tree.insert_left(11, 5)

print(binary_tree.to_list())

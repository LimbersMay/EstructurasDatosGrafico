from binary_search_tree import BinarySearchTree

# Crear árbol
tree = BinarySearchTree(60)

# Insertar nodos
tree.insert(12)
tree.insert(4)
tree.insert(1)
tree.insert(41)
tree.insert(29)
tree.insert(23)
tree.insert(37)
tree.insert(90)
tree.insert(71)
tree.insert(99)
tree.insert(84)

# Atravesar árbol
print(tree.pre_order())

from binary_tree import BinaryTree

# (A)
numbers = BinaryTree(27)

# (A(B))
numbers.insert_left(27, 14)

# (A(B, C))
numbers.insert_right(27, 47)

# (A(B(D), C))
numbers.insert_left(14, 7)

# (A(B(D(E)), C))
numbers.insert_right(7, 11)

# (A(B(D(E)), C(F)))
numbers.insert_left(7, 32)

# (A(B(D(E)), C(F, G)))
numbers.insert_right(7, 59)

# (A(B(D(E)), C(F, G(H))))
numbers.insert_left(59, 50)

# (A(B(D(E)), C(F, G(H, I))))
numbers.insert_right(59, 77)

print(numbers.pre_order())

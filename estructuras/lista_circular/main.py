from circular_list import CircularList

numbers = CircularList()
numbers.prepend(1)
numbers.prepend(2)
numbers.prepend(3)
numbers.prepend(4)
numbers.prepend(5)

print(numbers.traversal())

numbers.append(0)
numbers.append(-1)
numbers.append(-2)
numbers.append(-3)
numbers.append(-4)
numbers.append(-5)

print(numbers.traversal())

print(f"Buscar 0: {numbers._search(0)}")
print(f"Borrar -5: {numbers.remove(-5)}")
print(numbers.traversal())
print(f"Borrar 5: {numbers.remove(5)}")
print(numbers.traversal())
print(f"Borrar 0: {numbers.remove(0)}")
print(numbers.traversal())

print(f"Mover a la izquierda: {numbers.move_left()}")

print(numbers.traversal())

print(f"Mover a la derecha: {numbers.move_right()}")

print(numbers.traversal())

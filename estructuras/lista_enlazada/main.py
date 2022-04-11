from linked_list import LinkedList

ages: LinkedList[int] = LinkedList()

ages.append(25)
ages.append(32)
ages.append(14)
ages.append(33)

elements = ages.traversal()
first_node_data = ages.first
last_node_data = ages.last
size = len(ages)

print('Linked List Status:')
print(f"Head: {first_node_data}")
print(f"Tail: {last_node_data}")
print(f"Elements: {elements}")
print(f"Size: {size}")

# Ejemplos nuevos metodos
for x in range(1, 11):
    ages.append(x)

print('linked list status after deletions')
print(f"Search: {ages.search(25)}")
print(f"remove: {ages.remove(25)}")
try:
    print(f"Search: {ages.search(25)}")
except Exception as error:
    print(error)
print(f"prepend: {ages.prepend(69)}")
print(f"tail: {ages.last}")

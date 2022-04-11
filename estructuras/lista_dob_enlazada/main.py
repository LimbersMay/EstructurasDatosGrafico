from double_linked_list import DoubleLinkedList
from os import system


items = DoubleLinkedList()

while True:
    system('cls')
    option = input('Menu\n1. Insert new item\n2. Remove item\n3. Traverse items\n4. Exit')

    if option == '1':
        while True:
            system('cls')

            option = input('Insert new item\n1. Append\n 2. Prepend\n 3. Insert in position\n4. Menu')

            if option == '1':
                item = input('Item: ')

                print(f"{items.append(item)} insereted!")
                system('pause')

            elif option == '2':
                item = input('Item: ')

                print(f"{items.prepend(item)} inserted!")
                system('pause')

            elif option == '3':
                position = int(input('Position: '))

                item = input('Item: ')

                print(f"{items.append_in_position(item, position)} inserted!")
                system('pause')

            elif option == '4':
                break

            else:
                print('wrong number')
                system('pause')

    elif option == '2':
        while True:
            system('cls')
            option = input('Remove\n1. Head\n2. Tail\n 3. Specific item\n4. Menu')

            if option == '1':
                print(f"{items.remove_head()} was removed!")
                system('pause')

            elif option == '2':
                print(f"{items.remove_tail()} was removed!")
                system('pause')

            elif option == '3':
                item = input('Item: ')

                print(f"{items.remove(item)} was removed!")
                system('pause')

            elif option == '4':
                break

            else:
                print('wrong option')
                system('pause')

    elif option == '3':
        while True:
            system('cls')

            option = input('Traverse\n1. Forward\n2. Backwards\n3. Menu')

            if option == '1':
                print(items.traverse_forward())
                system('pause')

            elif option == '2':
                print(items.traverse_backwards())
                system('pause')

            elif option == '3':
                break

            else:
                print('wrong number')
                system('pause')

    elif option == '4':
        break

    else:
        print('wrong choice')
        system('pause')

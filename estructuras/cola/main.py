import os
from cola import Cola

# Bloque principal
# Menú
# 1- Ingresar un nuevo estudiante
# 2- Visualizar la cola
# 3- Eliminar estudiante
# 4- Eliminar estudiante en específico
# 5- Salir
estudiantes = Cola(3)
while True:
    os.system('cls')
    print('Menú')
    print('1- Ingresar un nuevo estudiante')
    print('2- Visualizar cola')
    print('3- Eliminar estudiante')
    print('4- Eliminar estudiante en específico')
    print('5- Salir')
    opcion = int(input('Ingrese una opción'))
    if opcion == 1:
        os.system('cls')
        print('INGRESAR ESTUDIANTE')
        nombre = input('Ingrese el nombre:')
        edad = int(input('Ingrese la edad: '))
        
        try:
            estudiantes.insertar(nombre, edad)
        except Exception as error:
            print('Ocurrió un error:')
            print(error)
        else: 
            resultado = estudiantes.recorrer()
            print('El estado de la cola es: ')
            print(resultado)

        os.system('pause')
    elif opcion == 2:
        os.system('cls')
        print('Los datos de la cola:')
        print(estudiantes)
        print('Los nodos de la cola son:')
        resultado = estudiantes.recorrer()
        print(resultado)
        os.system('pause')
    elif opcion == 3:
        os.system('cls')

        try: 
            nodo = estudiantes.eliminar()
        except Exception as error:
            print('Ocurrió un error')
            print(error)
            print('No hay nodos en la cola')
        else:   
            print('El nodo eliminado fue: ')
            print(nodo)
            print('Los nodos de la cola son:')
            resultado = estudiantes.recorrer()
            print(resultado)

        os.system('pause')
    elif opcion == 4:
        estudiante = input('Ingrese el nombre: ')
        while True:
            eliminado = estudiantes.eliminar()
            if estudiante == eliminado.nombre:
                break
            else:
                continue
    elif opcion == 5:
        break
    else:
        continue
from pila import Pila

peliculas_disponibles = Pila()

peliculas_disponibles.insertar('Venom 2')

print('segundo paso')
print(peliculas_disponibles.tamanio)
print(peliculas_disponibles.tope)

peliculas_disponibles.insertar('Paw Patrol: La pelicula')

print('tercer paso')
print(peliculas_disponibles.tamanio)
print(peliculas_disponibles.tope)
print(peliculas_disponibles.tope.siguiente)

peliculas_disponibles.insertar('Sin tiempo para morir')

print('cuarto paso')
print(peliculas_disponibles.tamanio)
print(peliculas_disponibles.tope)
print(peliculas_disponibles.tope.siguiente)
print(peliculas_disponibles.tope.siguiente.siguiente)

print('quito paso')
peliculas_disponibles.recorrer()

proximos_estrenos = Pila(3)

print('sexto paso')
print(proximos_estrenos.tamanio)
print(proximos_estrenos.tope)
print(proximos_estrenos.max)

try:
    proximos_estrenos.insertar('Spiderman')
    proximos_estrenos.insertar('Eternals')
    proximos_estrenos.insertar('Halloween Kills')
    proximos_estrenos.insertar('Msion imposible')
except Exception as error:
    print(f"Ocurrio un error al insertar\t{error}")

print(proximos_estrenos.tamanio)

# eliminar peliculas
peliculas_disponibles.eliminar()
print('paso 11')
print(peliculas_disponibles.tamanio)

peliculas_disponibles.eliminar()
print('paso 12')
print(peliculas_disponibles.tamanio)

peliculas_disponibles.eliminar()
print('paso 13')
print(peliculas_disponibles.tamanio)

try:
    peliculas_disponibles.eliminar()
    print(peliculas_disponibles.tamanio)
except Exception as error:
    print(f"Ocurrio un error al insertar\t{error}")



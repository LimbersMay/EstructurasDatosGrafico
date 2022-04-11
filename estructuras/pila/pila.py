from .nodo import Nodo

class Pila:
    
    def __init__(self, max = -1):
        self.tope = None
        self.tamanio = 0
        self.max = max

    def insertar(self, nombre_pelicula):
        if self.max == -1 or self.tamanio < self.max:
            nuevo_pelicula = Nodo(nombre_pelicula)
            nuevo_pelicula.siguiente = self.tope
            self.tope = nuevo_pelicula
            self.tamanio += 1
        else:
            raise Exception('Desbordamiento de pila')

    def recorrer(self):
        aux = self.tope
        while True:
            if aux == None:
                break
            else:
                print(aux)
                aux = aux.siguiente

    def eliminar(self):
        if self.tope == None:
            raise Exception('Subdesbordamiento de pila')
        else:
            aux = self.tope
            self.tope = self.tope.siguiente
            aux.siguiente = None
            self.tamanio -= 1
            return aux
from .nodo import Nodo

class Pila:
    
    def __init__(self, max = -1):
        self.tope = None
        self.tamanio = 0
        self.max = max

    def insertar(self, elemento):
        if self.max == -1 or self.tamanio < self.max:
            nuevo_nodo = Nodo(elemento)
            nuevo_nodo.siguiente = self.tope
            self.tope = nuevo_nodo
            self.tamanio += 1
        else:
            raise Exception('Desbordamiento de pila')

    def recorrer(self):
        aux = self.tope
        elementos = []
        while True:
            if aux == None:
                break
            else:
                elementos.append(aux.nombre)
                aux = aux.siguiente

        return elementos

    def eliminar(self):
        if self.tope == None:
            raise Exception('Subdesbordamiento de pila')
        else:
            aux = self.tope
            self.tope = self.tope.siguiente
            aux.siguiente = None
            self.tamanio -= 1
            return aux
    
    def buscar(self, elemento):
        aux = self.tope
        while True:
            if aux == None:
                break
            else:
                if aux.nombre == elemento:
                    return True
                else:
                    aux = aux.siguiente
        return False
    
    def buscar_nodo(self, elemento):
        # Buscamos la referencia en memoria del nodo
        aux = self.tope
        while True:
            if aux == None:
                break
            else:
                if aux.nombre == elemento:
                    return aux
                else:
                    aux = aux.siguiente
        
        return None
class Nodo:
    def __init__(self, elemento):
        # Parte amarilla
        self.data = elemento
        # Parte morada
        self.siguiente = None


class Pila:
    
    def __init__(self, max = -1):
        self.tope = None
        self._size = 0
        self.max = max

    def insertar(self, elemento):
        if self.max == -1 or self._size < self.max:
            nuevo_nodo = Nodo(elemento)
            nuevo_nodo.siguiente = self.tope
            self.tope = nuevo_nodo
            self._size += 1
        else:
            raise Exception('Desbordamiento de pila')

    def recorrer(self):
        aux = self.tope
        elementos = []
        while True:
            if aux == None:
                break
            else:
                elementos.append(aux.data)
                aux = aux.siguiente

        return elementos

    def eliminar(self):
        if self.tope == None:
            raise Exception('Subdesbordamiento de pila')
        else:
            aux = self.tope
            self.tope = self.tope.siguiente
            aux.siguiente = None
            self._size -= 1
            return aux
    
    def buscar(self, elemento):
        aux = self.tope
        while True:
            if aux == None:
                break
            else:
                if aux.data == elemento:
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
                if aux.data == elemento:
                    return aux
                else:
                    aux = aux.siguiente
        
        return None

    
    # Method that find a node in an index
    def search_position_node(self, index):
        if index < 0 or index >= self._size:
            raise Exception('Index out of range')
        aux = self.tope
        for i in range(index):
            aux = aux.siguiente
        return aux
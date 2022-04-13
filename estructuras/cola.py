class Nodo:
    def __init__(self,elemento):

        self.elemento = elemento
        self.siguiente = None
    
    def __str__(self):
        return f"{self.elemento}"


class Cola:
    def __init__(self,max = -1):
        self._size = 0
        self.frente = None
        self.fondo = None
        self.max = max

    def insertar(self,elemento):
        # 1. - construir el nodo
        nuevo = Nodo(elemento)

        # 2 - visitar el nodo
        # 3 - consultar si la cola esta vacia
        if self.frente == None and self.fondo == None:
            # 3.1  Frente y fondo apuntan a nuevo
            self.frente = nuevo
            self.fondo = nuevo

        elif self._size == self.max :
            raise Exception('No hay espacio, DESBORDAMIENTO DE PILA')
       
        else:
            self.fondo.siguiente =nuevo
            self.fondo = nuevo
            #4 - actualizar datos
        self._size += 1

    def recorrer(self):
        resultado = ''
        aux = self.frente
        while aux != None:
            # 2 - visitar el nodo
            resultado = resultado + str(aux) + '\n'
            # 3- mover el auxiliar
            aux = aux.siguiente

        return resultado
    def buscar_nodo(self,elemento):
        aux = self.frente
        vistos = 0
        while vistos < self._size:
            if elemento == aux.elemento:
                return aux
            else:
                aux = aux.siguiente
            vistos += 1
        

        if vistos == self._size:
            raise Exception ('Error, el elemento no existe')
    def eliminar(self):
        # 1- crear el auxiliar (señalar al frente)
        aux = self.frente
        
        if self._size == 0:
            raise Exception('SUBDESBORDAMIENTO DE COLA')
        elif self._size == 1:
            self.frente = None
            self.fondo = None
        else:
            # 2- Mover al frente al siguiente elemento 
            self.frente = aux.siguiente

            # 3- quitar enlaces
            aux.siguiente = None
        
        # 4- disminuir tamaño
        self._size -= 1

        # 5- devolver el nodo eliminado
        return aux

    def __str__(self):
        return f"Tamaño: {self._size}\nMax: {self.max}\nFrente: {self.frente}\nFondo: {self.fondo}"
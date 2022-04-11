class Nodo:
    def __init__(self, elemento):
        # Parte amarilla
        self.nombre = elemento
        # Parte morada
        self.siguiente = None

    def __str__(self):
        return str(self.nombre)
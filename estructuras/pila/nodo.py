class Nodo:
    def __init__(self, nombre_pelicula):
        # Parte amarilla
        self.nombre = nombre_pelicula
        # Parte morada
        self.siguiente = None

    def __str__(self):
        return self.nombre
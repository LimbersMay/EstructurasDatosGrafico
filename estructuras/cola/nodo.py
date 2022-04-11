class Nodo:
    def __init__(self,nombre,edad):

        self.nombre = nombre
        self.edad = edad


        self.siguiente = None
    

    def __str__(self):
        return f"{self.nombre} - {self.edad} años "

from frontend.lista_simple_template import ListaInterfaz
from estructuras.cola import Cola

class ColaInterfaz(ListaInterfaz):

    def __init__(self, master):
        super().__init__(master)

        self.lista = Cola()
    
    def insertar(self, elemento):
        self.lista.insertar(elemento)

        self.dibujar_lista()
    
    def eliminar(self):
        self.lista.eliminar()

        self.dibujar_lista()
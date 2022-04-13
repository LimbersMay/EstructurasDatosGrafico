from frontend.lista_interfaz import ListaInterfaz
from estructuras.cola.cola import Cola

class ColaInterfaz(ListaInterfaz):

    def __init__(self, master):
        super().__init__(master)

        self.cola = Cola()
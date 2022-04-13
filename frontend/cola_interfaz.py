from frontend.lista_simple_template import ListaInterfaz
from estructuras.cola import Cola

class ColaInterfaz(ListaInterfaz):

    def __init__(self, master):
        super().__init__(master)

        self.cola = Cola()
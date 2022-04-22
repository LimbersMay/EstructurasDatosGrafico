class ArbolBinarioInformacion:
    def __init__(self, nodos_nivel, root, cant_nodes, profundidad, nodo_seleccionado=None):
        self.nodos_nivel = nodos_nivel
        self.root = root
        self.cant_nodes = cant_nodes
        self.profundidad = profundidad
        self.nodo_seleccionado = nodo_seleccionado

    def get_nodos_nivel(self):
        return self.nodos_nivel

    def get_root(self):
        return self.root

    def get_cantidad_nodos(self):
        return self.cant_nodes

    def get_profundidad(self):
        return self.profundidad

    def set_seleccionado(self, booleano):
        self.nodo_seleccionado = booleano

    def get_seleccionado(self):
        return self.nodo_seleccionado

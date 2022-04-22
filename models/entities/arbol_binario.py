class ArbolBinarioInformacion:
    def __init__(self, root, cant_nodes, profundidad, nodo_seleccionado=None):
        self.nodos_nivel: [NodoInformacion] = []
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


class NodoInformacion:
    def __init__(self, data, id, hijo_izquierdo, hijo_derecho):
        self.data = data
        self.id = id

        self.hijo_izquierdo: bool = hijo_izquierdo
        self.hijo_derecho: bool = hijo_derecho

    def get_data(self):
        return self.data

    def get_id(self):
        return self.id

    def tiene_hijo_izquierdo(self):
        return self.hijo_izquierdo

    def tiene_hijo_derecho(self):
        return self.hijo_derecho

    def is_leaf(self):
        return not self.tiene_hijo_izquierdo() and not self.tiene_hijo_derecho()

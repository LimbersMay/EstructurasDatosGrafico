class InformacionArbolBinario:
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


class BinaryTreeModelTemplate:
    def __init__(self, tree):
        self.tree = tree
        self.fichero = None

    def insertar_raiz(self, valor):
        self.tree.insert_root(valor)

        return self.obtener_informacion()

    def buscar(self, valor):
        nodo_buscado = self.tree.search(valor).get_data()

        arbol_informacion = self.obtener_informacion()
        arbol_informacion.set_seleccionado(nodo_buscado)

        return arbol_informacion

    def eliminar(self, valor):
        self.tree.remove_node(valor)

        return self.obtener_informacion()

    def obtener_informacion(self):
        nodes_level = []
        root = self.tree.get_root()
        cantidad_nodos = self.tree.count_nodes()
        profundidad = self.tree.max_depth()

        # Obtenemos los nodos de todos los niveles
        for i in range(self.tree.max_depth()):
            nodes_level.append(self.tree.level_nodes(i))

        return InformacionArbolBinario(nodes_level, root, cantidad_nodos, profundidad)

    # ---- FUNCIONES PARA INTERACTUAR CON EL FICHERO DE INFORMACIÓN ------
    def cargar_opciones(self):
        # Obtenemos todos los elementos de árbol del Json
        elementos_arbol = self.fichero.obtener_elementos()
        nombres_arboles = [nombre for nombre in elementos_arbol]

        return nombres_arboles

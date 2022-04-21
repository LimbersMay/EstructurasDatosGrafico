from estructuras.binary_tree import BinaryTree


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


class SimpleBinaryTreeModel:
    def __init__(self, tree):
        self.tree = tree

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


class BinaryTreeModel(SimpleBinaryTreeModel):
    def __init__(self, tree):
        super().__init__(tree)

    def insertar_izquierda(self, valor, padre):
        self.tree.insert_left(valor, padre)

        return self.obtener_informacion()

    def insertar_derecha(self, valor, padre):
        self.tree.insert_right(valor, padre)

        return self.obtener_informacion()


class SearchBinaryTreeModel(SimpleBinaryTreeModel):
    def __init__(self, tree):
        super().__init__(tree)

    def insertar(self, valor):
        self.tree.insert(valor)

        return self.obtener_informacion()
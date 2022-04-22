from models.entities.arbol_binario import ArbolBinarioInformacion


class ArbolBinarioModelTemplate:
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
        nodos_nivel = []  # Lista de nodos de un nivel
        root = self.tree.get_root()  # Raiz del árbol
        cantidad_nodos = self.tree.count_nodes()  # Cantidad de nodos del árbol
        profundidad = self.tree.max_depth()  # Profundidad del árbol

        # Obtenemos los nodos de todos los niveles
        for i in range(self.tree.max_depth()):
            nodos_nivel.append(self.tree.level_nodes(i))

        return ArbolBinarioInformacion(nodos_nivel, root, cantidad_nodos, profundidad)

    # ---- FUNCIONES PARA INTERACTUAR CON EL FICHERO DE INFORMACIÓN ------
    def cargar_opciones(self):
        # Obtenemos todos los elementos de árbol del Json
        elementos_arbol = self.fichero.obtener_elementos()
        nombres_arboles = [nombre for nombre in elementos_arbol]

        return nombres_arboles

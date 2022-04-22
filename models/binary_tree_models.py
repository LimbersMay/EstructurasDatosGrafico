from .fichero import Fichero


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


class BinaryTreeModel(SimpleBinaryTreeModel):
    def __init__(self, tree):
        super().__init__(tree)

        self.fichero = Fichero("recursos/datos/arboles_binarios.json")

    def insertar_izquierda(self, valor, padre):
        self.tree.insert_left(valor, padre)

        return self.obtener_informacion()

    def insertar_derecha(self, valor, padre):
        self.tree.insert_right(valor, padre)

        return self.obtener_informacion()

    # Operaciones para guardar el árbol dentro de un fichero Json
    def guardar(self, nombre):

        # Para guardar el árbol en el Json obtenemos todos los nodos de cada nivel del arbol
        # ejemplo:
        # 0: [5] -> raíz
        # 1: [2, 3] -> hijos de raíz
        # 2: [8, 9, 4, 6] -> hijos de hijos de raíz

        nodos_niveles = self.tree.to_matrix()
        niveles_dic = {}

        # Creamos un diccionario con la información de los niveles del árbol
        for i in range(len(nodos_niveles)):
            niveles_dic[i] = nodos_niveles[i]

        # Guardamos ese diccionario en el Json con la información de los niveles
        # Ejemplo:
        # {
        # "arbol1" : {
        #              0: [5],
        #              1: [2, 3],
        #              2: [8, 9, 4, 6]
        # }

        # Guardamos la información en el Json
        self.fichero.guardar_informacion(nombre, niveles_dic)

        # Obtenemos la lista de las claves del diccionario
        elementos_arbol = self.fichero.obtener_elementos()
        nombres_arboles = [nombre for nombre in elementos_arbol]

        return nombres_arboles

    def cargar(self, nombre):

        # Para cargar un árbol obtenemos la información del Json de los niveles de este
        niveles_arbol = self.fichero.obtener_valor(nombre)

        # Ejemplo
        # "arbol1" : {
        #              0: [5],      <-- Nodo raíz
        #              1: [2, 3],   <-- Nodos del nivel 1
        #              2: [8, 9, 4, 6]  <-- Nodos del nivel 2

        # Antes de cargar la información, debemos limpiar el árbol
        self.tree.clear()

        # Lo recorremos y los insertamos en el árbol
        for nivel in niveles_arbol:
            self.tree.insert_in_level(int(nivel), niveles_arbol[nivel])

        return self.obtener_informacion()

    def remover(self, nombre):
        # Removelos la clave del Json
        self.fichero.eliminar_elemento(nombre)

        return self.cargar_opciones()


class SearchBinaryTreeModel(SimpleBinaryTreeModel):
    def __init__(self, tree):
        super().__init__(tree)

        self.fichero = Fichero("recursos/datos/arboles_busqueda.json")

    def insertar(self, valor):
        self.tree.insert(valor)

        return self.obtener_informacion()

    def guardar(self, nombre):
        # Obtenemos una lista de los árboles en orden de niveñ
        nodos_niveles = self.tree.to_list()

        # Guardamos la información en el Json
        self.fichero.guardar_informacion(nombre, nodos_niveles)

        # Obtenemos los elementos de árboles de búsqueda del Json
        elementos_arbol = self.fichero.obtener_elementos()
        nombres_arboles = [nombre for nombre in elementos_arbol]

        return nombres_arboles

    def cargar(self, nombre):

        # Obtenemos la lista de nodos del árbol dentro del Json
        nodos_arbol = self.fichero.obtener_valor(nombre)

        # Limpiamos el árbol actual
        self.tree.clear()

        # Los insertamos en el árbol
        for nodo in nodos_arbol:
            self.tree.insert(nodo)

        return self.obtener_informacion()

    def remover(self, nombre):
        pass

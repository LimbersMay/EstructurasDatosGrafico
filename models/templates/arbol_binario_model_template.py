from models.entities.arbol_binario import ArbolBinarioInformacion, NodoInformacion


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

        # Datos necesarios para el árbol
        # 1. Raíz
        # 2. Nodos: [NodoInformacion]
        # 3. Profundidad

        # Datos necesarios para cada nodo (NodoInformacion)
        # 1. Dato
        # 2. Id
        # 3. Tiene hijo derecho: bool
        # 4. Tiene hijo izquierdo: bool

        root = self.tree.get_root()  # Raiz del árbol
        cantidad_nodos = self.tree.count_nodes()  # Cantidad de nodos del árbol
        profundidad = self.tree.max_depth()  # Profundidad del árbol

        arbol_informacion = ArbolBinarioInformacion(root, cantidad_nodos, profundidad)

        # Obtenemos los nodos de todos los niveles
        for i in range(self.tree.max_depth()):
            nodos_nivel = self.tree.level_nodes(i, references=True)

            nodos_nivel_informacion = []
            # Recorremos cada nodo y obtenemos los datos que necesitamos
            for nodo in nodos_nivel:

                # Obtenenmos todos los datos de cada nodo que necesitamos
                data = nodo.get_data()
                id_nodo = id(nodo)

                tiene_hijo_izquierdo = False
                tiene_hijo_derecho = False

                # Comprobamos que este nodo no sea uno de relleno que usamos para completar el árbol
                if nodo.left is not None:
                    if nodo.left.data is not None:
                        tiene_hijo_izquierdo = True

                if nodo.right is not None:
                    if nodo.right.data is not None:
                        tiene_hijo_derecho = True

                # Creamos un objeto nodo información y lo agregamos a la lista
                nodo_informacion = NodoInformacion(data, id_nodo, tiene_hijo_izquierdo, tiene_hijo_derecho)
                nodos_nivel_informacion.append(nodo_informacion)

            arbol_informacion.nodos_nivel.append(nodos_nivel_informacion)

            # Al final tendremos una matriz con los nodos de información de cada nivel
            # Ejemplo:
            # [
            #   [nodo_informacion_nivel_0, nodo_informacion_nivel_1, nodo_informacion_nivel_2, ...], -> Raíz
            #   [nodo_informacion_nivel_0, nodo_informacion_nivel_1, nodo_informacion_nivel_2, ...], -> Nivel 1
            #   [nodo_informacion_nivel_0, nodo_informacion_nivel_1, nodo_informacion_nivel_2, ...], -> Nivel 2
            #   ...
            # ]

        return arbol_informacion

    # ---- FUNCIONES PARA INTERACTUAR CON EL FICHERO DE INFORMACIÓN ------
    def cargar_opciones(self):
        # Obtenemos todos los elementos de árbol del Json
        elementos_arbol = self.fichero.obtener_elementos()
        nombres_arboles = [nombre for nombre in elementos_arbol]

        return nombres_arboles

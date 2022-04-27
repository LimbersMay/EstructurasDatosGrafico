from .fichero import Fichero
from .templates.arbol_binario_model_template import ArbolBinarioModelTemplate


class ArbolBinarioBusquedaModel(ArbolBinarioModelTemplate):
    def __init__(self, tree):
        super().__init__(tree)

        self.fichero = Fichero("recursos/datos/arboles_busqueda.json")

    def insertar(self, valor):

        # Comprobamos si el valor es un entero
        if isinstance(valor, int):
            self.tree.insert(valor)

            return self.obtener_informacion()

        # Comprobamos si el valor de la cadena es un digito
        elif valor.isdigit():
            self.tree.insert(int(valor))

            return self.obtener_informacion()

        # Comprobamos si es un valor flotante
        try:
            valor = float(valor)
            self.tree.insert(valor)

            return self.obtener_informacion()

        except ValueError:
            pass

        # De llegar aquí, damos por hecho que el valor es una cadena
        self.tree.insert(valor)
        return self.obtener_informacion()

    # -------- OPERACIONES QUE INTERACTUAN CON EL FICHERO DEL ÁRBOL --------
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
        # Removemos el árbol del Json
        self.fichero.eliminar_elemento(nombre)

        # Devolvemos la información de las estructuras del json
        return self.cargar_opciones()

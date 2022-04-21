from .fichero import Fichero


# Models for the lists
# Responsabilidad: Interactuar directamente con la estructura y con el fichero de configuración
class ListModel:
    def __init__(self, list_name):
        self.list = list_name
        self.fichero = None

    def insertar_inicio(self, elemento):
        self.list.prepend(elemento)

        return self.obtener_informacion()

    def insertar_final(self, elemento):
        self.list.append(elemento)

        return self.obtener_informacion()

    def eliminar_inicio(self):
        self.list.remove_head()

        return self.obtener_informacion()

    def eliminar_final(self):
        self.list.remove_tail()

        return self.obtener_informacion()

    def buscar(self, elemento):
        nodo_buscado = self.list.search(elemento)

        informacion = self.obtener_informacion()
        informacion.append(nodo_buscado)

        return informacion

    def guardar(self, nombre):
        # Obtenemos todos los elementos de la lista actual
        lista_elementos = self.list.to_list()

        # Guardamos en el Json la clave con su valor
        # Ejemolo: lista_elementos = {'nombre': 'lista_elementos'}
        self.fichero.guardar_informacion(nombre, lista_elementos)

        # Obtenemos todos los elementos lista del fichero
        lista_elementos_fichero = self.fichero.obtener_elementos()

        # Obtenemos solamente las claves (Nombres de las listas) de los elementos
        lista_nombres_elementos = [nombre for nombre in lista_elementos_fichero]

        return lista_nombres_elementos

    def cargar(self, nombre):

        # Obtenemos la lista de elementos del fichero del nombre pasado por parámetro
        lista_elementos = self.fichero.obtener_valor(nombre)

        # Vaciamos la list actual
        self.list.clear()
        
        # Insertamos los elementos de la lista en la lista actual
        for elemento in lista_elementos:
            self.list.append(elemento)
            
        return self.obtener_informacion()

    def eliminar(self, nombre):
        self.fichero.eliminar_elemento(nombre)

        return self.cargar_opciones()

    def cargar_opciones(self):
        # Obtenemos todos los elementos lista del fichero
        lista_elementos_fichero = self.fichero.obtener_elementos()
        
        # Obtenemos solamente las claves (Nombres de las listas) de los elementos
        lista_nombres = [nombre for nombre in lista_elementos_fichero]
        
        return lista_nombres

    def obtener_informacion(self):
        return [self.list.get_nodes_information(), self.list.get_list_information()]


class SimpleListModel(ListModel):
    def __init__(self, list_name):
        super().__init__(list_name)

        self.fichero = Fichero("recursos/datos/listas_enlazadas.json")


class DoubleLinkedListModel(ListModel):
    def __init__(self, list_name):
        super().__init__(list_name)

        self.fichero = Fichero("recursos/datos/listas_dob_enlazadas.json")

    def insertar_por_indice(self, elemento, indice):
        self.list.append_in_position(elemento, indice)

        return self.obtener_informacion()

    def eliminar_por_indice(self, indice):
        self.list.remove_in_position(indice)

        return self.obtener_informacion()


class CircularListModel(ListModel):
    def __init__(self, list_name):
        super().__init__(list_name)

        self.fichero = Fichero("recursos/datos/listas_circulares.json")

    def rotar_izquierda(self):
        self.list.rotate_left()

        return self.obtener_informacion()

    def rotar_derecha(self):
        self.list.rotate_right()

        return self.obtener_informacion()

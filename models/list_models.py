# Models for the lists
# Responsabilidad: Interactuar directamente con la estructura y con el fichero de configuración
class ListModel:
    def __init__(self, list_name):
        self.list = list_name

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

    def obtener_informacion(self):
        return [self.list.get_nodes_information(), self.list.get_list_information()]


class SimpleListModel(ListModel):
    def __init__(self, list_name):
        super().__init__(list_name)


class DoubleLinkedListModel(ListModel):
    def __init__(self, list_name):
        super().__init__(list_name)

    def insertar_por_indice(self, elemento, indice):
        self.list.append_in_position(elemento, indice)

        return self.obtener_informacion()

    def eliminar_por_indice(self, indice):
        self.list.remove_in_position(indice)

        return self.obtener_informacion()


class CircularListModel(ListModel):
    def __init__(self, list_name):
        super().__init__(list_name)

    def rotar_izquierda(self):
        self.list.rotate_left()

        return self.obtener_informacion()

    def rotar_derecha(self):
        self.list.rotate_right()

        return self.obtener_informacion()


#



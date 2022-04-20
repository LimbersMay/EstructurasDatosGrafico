from .list_controller_template import ListController


class SimpleListController(ListController):
    def __init__(self, model, view):
        super().__init__(model, view)


class DoublyLinkedListController(ListController):
    def __init__(self, model, view):
        super().__init__(model, view)

    def insertar_por_indice(self, dato, indice):

        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.insertar_por_indice(dato, indice)
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print(e)

    def eliminar_por_indice(self, indice):

        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.eliminar_por_indice(indice)
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print(e)


class CircularListController(ListController):
    def __init__(self, model, view):
        super().__init__(model, view)

    def rotar_izquierda(self):

        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.rotar_izquierda()
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print(e)

    def rotar_derecha(self):

        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.rotar_derecha()
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print(e)

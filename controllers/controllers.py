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


# Controller for Stack
class StackController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def insert(self, valor):

        try:
            # Intentamos mostrar la información
            informacion_pila = self.model.push(valor)
            self.view.actualizar(informacion_pila)

        except Exception as e:
            print(e)

    def remove(self):
        try:
            # Intentamos mostrar la información
            informacion_pila = self.model.pop()
            self.view.actualizar(informacion_pila)

        except Exception as e:
            print(e)

    def search(self, valor):
        try:
            # Intentamos mostrar la información
            informacion_pila = self.model.search(valor)
            self.view.actualizar(informacion_pila)

        except Exception as e:
            print(e)


# Controller for Queue
class QueueController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def insert(self, valor):

        try:
            # Intentamos mostrar la información
            informacion_cola = self.model.enqueue(valor)
            self.view.actualizar(informacion_cola)

        except Exception as e:
            print(e)

    def remove(self):

        try:
            # Intentamos mostrar la información
            informacion_cola = self.model.dequeue()
            self.view.actualizar(informacion_cola)

        except Exception as e:
            print(e)

    def search(self, valor):
        try:
            # Intentamos mostrar la información
            informacion_cola = self.model.search(valor)
            self.view.actualizar(informacion_cola)

        except Exception as e:
            print(e)

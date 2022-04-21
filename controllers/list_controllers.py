# Responsabiliddad: Informar al modelo de los cambios en los controles
class ListController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    # Métodos comunes las estructuras
    def insertar_inicio(self, valor):

        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.insertar_inicio(valor)
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    def insertar_final(self, valor):

        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.insertar_final(valor)
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    def eliminar_inicio(self):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.eliminar_inicio()
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    def eliminar_final(self):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.eliminar_final()
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    # Operaciones que se realizarán con el Json
    def buscar(self, valor):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.buscar(valor)
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    def guardar(self):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.guardar()
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    def cargar(self):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.cargar()
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    def eliminar(self):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.guardar()
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)


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

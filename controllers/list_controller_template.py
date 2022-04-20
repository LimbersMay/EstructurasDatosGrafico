# Responsabiliddad: Informar al modelo de los cambios en los controles
import traceback


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

    def buscar(self, valor):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.buscar(valor)
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

# Responsabiliddad: Informar al modelo de los cambios en los controles
class SimpleTreeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def insertar_raiz(self, dato):
        try:
            informacion_arbol = self.model.insertar_raiz(dato)
            self.view.mostrar_arbol(informacion_arbol)

        except Exception as e:
            print("Error:", e)

    def buscar(self, dato):
        try:
            informacion_arbol = self.model.buscar(dato)
            self.view.mostrar_arbol(informacion_arbol)

        except Exception as e:
            print("Error:", e)

    def eliminar(self, dato):
        try:
            informacion_arbol = self.model.eliminar(dato)
            self.view.mostrar_arbol(informacion_arbol)

        except Exception as e:
            print("Error:", e)


class BinaryTreeController(SimpleTreeController):
    def __init__(self, model, view):
        super().__init__(model, view)

    def insertar_izquierda(self, dato, padre):
        try:
            informacion_arbol = self.model.insertar_izquierda(dato, padre)
            self.view.mostrar_arbol(informacion_arbol)

        except Exception as e:
            print("Error:", e)

    def insertar_derecha(self, dato, padre):
        try:
            informacion_arbol = self.model.insertar_derecha(dato, padre)
            self.view.mostrar_arbol(informacion_arbol)

        except Exception as e:
            print("Error:", e)


class SearchBinaryTreeController(SimpleTreeController):
    def __init__(self, model, view):
        super().__init__(model, view)
        self.model = model
        self.view = view

    def insertar(self, dato):
        try:
            informacion_arbol = self.model.insertar(dato)
            self.view.mostrar_arbol(informacion_arbol)

        except Exception as e:
            print("Error:", e)

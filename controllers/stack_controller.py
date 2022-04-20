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
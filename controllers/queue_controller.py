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

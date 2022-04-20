# Model for the Stack
class StackModel:
    def __init__(self, stack):
        self.stack = stack

    def push(self, elemento):
        self.stack.push(elemento)

        return self.obtener_informacion()

    def pop(self):
        self.stack.pop()

        return self.obtener_informacion()

    def search(self, elemento):
        nodo_buscado = self.stack.search(elemento)

        informacion = self.obtener_informacion()
        informacion.append(nodo_buscado)

        return informacion

    def obtener_informacion(self):
        return [self.stack.get_nodes_information(), self.stack.get_stack_information()]
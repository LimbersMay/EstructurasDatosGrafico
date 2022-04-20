# Models for the lists
from .list_model_template import ListModel


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


# Model for the queue
class QueueModel:
    def __init__(self, queue):
        self.queue = queue

    def enqueue(self, elemento):
        self.queue.enqueue(elemento)

        return self.obtener_informacion()

    def dequeue(self):
        self.queue.dequeue()

        return self.obtener_informacion()

    def search(self, elemento):
        nodo_buscado = self.queue.search(elemento)

        informacion = self.obtener_informacion()
        informacion.append(nodo_buscado)

        return informacion

    def obtener_informacion(self):
        return [self.queue.get_nodes_information(), self.queue.get_queue_information()]

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

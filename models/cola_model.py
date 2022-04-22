from .fichero import Fichero


# Model for the queue
class ColaModel:
    def __init__(self, queue):
        self.queue = queue
        self.fichero = Fichero('recursos/datos/colas.json')

    def enqueue(self, nombre):
        self.queue.enqueue(nombre)

        return self.obtener_informacion()

    def dequeue(self):
        self.queue.dequeue()

        return self.obtener_informacion()

    def search(self, nombre):
        nodo_buscado = self.queue.search(nombre)

        informacion = self.obtener_informacion()
        informacion.append(nodo_buscado)

        return informacion

    def guardar(self, nombre):
        # Obtenemos todos los elementos de la cola en una lista
        lista_elementos = self.queue.to_list()
        # Guardamos la información proporcionada en el Json con el siguiente formato
        # {
        # 'cola1': [1, 2, 3, 4, 5, 6, 7]
        # }
        self.fichero.guardar_informacion(nombre, lista_elementos)

        # Obtenemos todos los elementos cola del fichero json
        # {
        # clave :    valor
        # 'cola1: [1, 2, 3],
        # 'cola2: [5, 3, 9]
        # }
        elementos_cola = self.fichero.obtener_elementos()

        # Listamos solamente las claves de las colas
        lista_nombres = [elemento for elemento in elementos_cola]

        return lista_nombres

    def cargar(self, nombre):
        # Obtenemos la lista que almacena la clave que deseamos
        cola_elementos = self.fichero.obtener_valor(nombre)

        # Vacíamos la cola existente
        self.queue.clear()

        # Añadimos los elementos
        for elemento in cola_elementos:
            print("Elemento a encolar: ", elemento)
            self.queue.enqueue(elemento)

        print("Despues de encolar: ", self.queue.to_list())

        return self.obtener_informacion()

    def eliminar(self, nombre):
        self.fichero.eliminar_elemento(nombre)

        return self.cargar_opciones()

    def cargar_opciones(self):
        # Obtenemos todos los elementos de las colas
        elementos_cola = self.fichero.obtener_elementos()

        # {
        #  clave:    valor
        # 'cola1: [1, 2, 3],
        # 'cola2: [5, 3, 9]
        # }

        # Obtenenmos solo las claves de los diccionarios
        lista_nombres = [elemento for elemento in elementos_cola]

        return lista_nombres

    def obtener_informacion(self):
        return [self.queue.get_nodes_information(), self.queue.get_queue_information()]

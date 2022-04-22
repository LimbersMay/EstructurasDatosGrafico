class EstructuraLinealInformacion:
    def __init__(self, head, tail, size, max_size=None):
        self.head = head
        self.tail = tail
        self.size = size
        self.max_size = max_size

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def get_size(self):
        return self.size

    def get_max(self):
        return self.max_size


class NodoInformacion:
    def __init__(self, data, id_node):
        self.data = data
        self.id = id_node

    def get_data(self):
        return self.data

    def get_id(self):
        return self.id

    def set_data(self, data):
        self.data = data

    def set_id(self, reference):
        self.id = reference

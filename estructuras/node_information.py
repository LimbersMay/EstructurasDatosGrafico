
class NodeInformation:
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

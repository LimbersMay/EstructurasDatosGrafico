class LinealStructureInformation:
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

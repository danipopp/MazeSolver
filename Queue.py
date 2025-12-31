class FIFO:
    def __init__(self):
        self.iteams = []

    def enqueue(self, item):
        self.iteams.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.iteams.pop(0)
        return None

    def is_empty(self):
        return len(self.iteams) == 0
class Queue:
    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def delete(self):
        if self.len_queue > 0:
            elem = self.queue.pop(0)
            self.len_queue -= 1
            return elem
        else:
            print("Queue is empty")

    def add(self, elem) -> None:
        self.queue.append(elem)
        self.len_queue += 1

    def peek(self):
        if self.len_queue > 0:
            return self.queue[-1]
        else:
            print("Queue is empty")

    def is_empty(self) -> bool:
        return self.len_queue == 0

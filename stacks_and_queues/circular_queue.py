class CircularQueue:
    def __init__(self):
        self.len_q = 0
        self.max_len = 3
        self.queue = [None] * self.max_len
        self.front = 0
        self.rear = 0

    def deque(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue element")
            return False
        else:
            self.len_q -= 1
            elem = self.queue[self.front]
            self.front += 1

            if self.front == self.max_len:
                self.front = 0
            return elem

    def enqueue(self, elem):
        if self.is_full():
            print("Queue is full, cannot enqueue element")
            return False
        else:
            self.len_q += 1
            self.queue[self.rear] = elem
            self.rear += 1

            if self.rear == self.max_len:
                self.rear = 0

    def is_empty(self) -> bool:
        return self.len_q == 0

    def is_full(self) -> bool:
        return self.len_q == self.max_len


cq = CircularQueue()
cq.enqueue("first")
cq.enqueue("second")
cq.enqueue("third")
cq.enqueue("fourth")
print(cq.deque())
print(cq.deque())

cq.enqueue("fourth")

print(cq.deque())
print(cq.deque())
print(cq.deque())

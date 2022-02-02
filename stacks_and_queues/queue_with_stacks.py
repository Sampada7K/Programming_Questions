from stacks_and_queues.stack import Stack


class QueueWithStacks:
    def __init__(self):
        self.enq_stack = Stack()
        self.deq_stack = Stack()
        self.len_q = 0

    def enq(self, elem):
        self.enq_stack.push(elem)
        self.len_q += 1

    def deq(self):
        # if q is empty
        if self.is_empty():
            print("Cannot deque element, queue is empty")
            return False

        # deq stack is empty
        if self.deq_stack.is_empty():
            # Transfer elements from enq stack to deq stack
            for i in range(self.enq_stack.len_stack):
                self.deq_stack.push(self.enq_stack.pop())

        # pop element from the deq_stack
        elem = self.deq_stack.pop()
        self.len_q -= 1
        return elem

    def is_empty(self):
        return self.len_q == 0


qws = QueueWithStacks()
qws.enq("first")
qws.enq("second")
qws.enq("third")
print(qws.deq())
print(qws.deq())
qws.enq("fourth")
print(qws.len_q)

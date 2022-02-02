class Stack:
    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def pop(self):
        if self.len_stack > 0:
            elem = self.stack.pop()
            self.len_stack -= 1
            return elem
        else:
            print("Stack is empty")

    def push(self, elem) -> None:
        self.stack.append(elem)
        self.len_stack += 1

    def peek(self):
        if self.len_stack > 0:
            return self.stack[-1]
        else:
            print("Stack is empty")

    def is_empty(self) -> bool:
        return self.len_stack == 0

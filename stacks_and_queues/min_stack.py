class MinStack:
    def __init__(self):
        self.stack = []
        self.len_stack = 0
        self.min_elem = False

    def pop(self):
        if self.len_stack > 0:
            elem = self.stack.pop()[0]
            self.len_stack -= 1

            if self.len_stack >= 1:
                self.min_elem = self.stack[-1][1]

            if self.len_stack == 0:
                self.min_elem = False
            return elem
        else:
            print("Stack is empty")

    def push(self, elem) -> None:
        if self.len_stack == 0:
            self.min_elem = elem
        else:
            self.min_elem = min(self.min_elem, elem)

        self.stack.append((elem, self.min_elem))
        self.len_stack += 1

    def peek(self):
        if self.len_stack > 0:
            return self.stack[-1]
        else:
            print("Stack is empty")

    def is_empty(self) -> bool:
        return self.len_stack == 0


s = MinStack()
print (f'Min elem is {s.min_elem}')
s.push(7)
print(f'Min elem is {s.min_elem}')
s.push(5)
print(f'Min elem is {s.min_elem}')
s.push(8)
print(f'Min elem is {s.min_elem}')

print(f'Popped elem is {s.pop()}')
print(f'Min elem is {s.min_elem}')
print(f'Popped elem is {s.pop()}')
print(f'Min elem is {s.min_elem}')
print(f'Popped elem is {s.pop()}')
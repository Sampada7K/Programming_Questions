from stacks_and_queues.stack import Stack


class SetOfStacks:
    def __init__(self):
        self.set_of_stacks = []
        self.len_set_of_stack = 1
        self.current_stack = Stack()
        self.set_of_stacks.append(self.current_stack)

    def push(self, plate):
        # Current Stack is full
        if self.current_stack.len_stack >= 2:
            self.len_set_of_stack += 1
            self.current_stack = Stack()
            self.set_of_stacks.append(self.current_stack)

        # Current Stack is full, push to newly created current_stack else push to the existing current_stack
        self.current_stack.push(plate)

    def pop(self):
        # Current stack is empty
        if self.current_stack.is_empty():
            # There are previous plate stacks
            if self.len_set_of_stack > 1:
                self.set_of_stacks.pop()
                self.len_set_of_stack -= 1
                self.current_stack = self.set_of_stacks[-1]
                return self.current_stack.pop()
            # There are no previous plate stacks
            else:
                print("No plate to pop")
                return False

        # Current stack is not empty
        else:
            return self.current_stack.pop()


sp = SetOfStacks()
print(f'Current set of stack length is {sp.len_set_of_stack}')
sp.push("plate1")
sp.push("plate2")
for i in range(2):
    print(sp.pop())
sp.pop()
print(f'Current set of stack length is {sp.len_set_of_stack}')
sp.push("plate1")
sp.push("plate2")
sp.push("plate3")
print(f'Current set of stack length is {sp.len_set_of_stack}')
sp.push("plate4")
sp.push("plate5")
print(f'Current set of stack length is {sp.len_set_of_stack}')
sp.push("plate6")
sp.push("plate7")
print(f'Current set of stack length is {sp.len_set_of_stack}')
sp.push("plate8")
sp.push("plate9")
print(f'Current set of stack length is {sp.len_set_of_stack}')
sp.push("plate10")
sp.push("plate11")
print(f'Current set of stack length is {sp.len_set_of_stack}')
sp.push("plate12")
print(f'Current set of stack length is {sp.len_set_of_stack}')

for i in range(12):
    print(sp.pop())

print(sp.pop())

from stacks_and_queues.stack import Stack


def sort_stack(stack1: Stack):
    temp_stack = Stack()
    print(f'Len of original stack is {stack1.len_stack}')
    while not stack1.is_empty():
        tmp = stack1.pop()
        print(f'Tmp is {tmp}')

        while not temp_stack.is_empty() and temp_stack.peek() > tmp:
            print(f'Len of temp stack is {temp_stack.len_stack}')
            stack1.push(temp_stack.pop())
        temp_stack.push(tmp)

    while not temp_stack.is_empty():
        stack1.push(temp_stack.pop())

    return stack1


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)


sorted_stack = sort_stack(s)

for i in range(sorted_stack.len_stack):
    print(sorted_stack.pop())

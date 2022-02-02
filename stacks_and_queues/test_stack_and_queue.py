from stacks_and_queues.stack import Stack
from stacks_and_queues.queue import Queue

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1.is_empty())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.is_empty())


q1 = Queue()
q1.add(1)
q1.add(2)
q1.add(3)
print(q1.is_empty())
print(q1.delete())
print(q1.delete())
print(q1.delete())
print(q1.delete())
print(q1.is_empty())


'''Stack:
A stack is a data structure that follows the Last In, 
First Out (LIFO) principle, meaning the last element added
is the first one to be removed. Think of it like a stack of
plates where you can only take the top one.
'''
# Basic Stack Implementation
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Pop elements from the stack
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2



'''Queue:
A queue is a data structure that follows the First In, First Out (FIFO) 
principle, meaning the first element added is the first one to be removed. 
It's similar to waiting in a queue for a bus.
'''
## Basic Queue Implementation in Python
from collections import deque

queue = deque()

# Enqueue elements into the queue
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue elements from the queue
print(queue.popleft())  # Output: 1
print(queue.popleft())  # Output: 2

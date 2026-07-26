from collections import deque


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(list(self.items))


print("=== Stack Demo ===")

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:")
stack.display()

print("Top item:")
print(stack.peek())

print("Popped item:")
print(stack.pop())

print("Stack after pop:")
stack.display()


print("\n=== Queue Demo ===")

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue:")
queue.display()

print("Front item:")
print(queue.peek())

print("Dequeued item:")
print(queue.dequeue())

print("Queue after dequeue:")
queue.display()
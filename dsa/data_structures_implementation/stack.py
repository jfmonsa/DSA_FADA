class Stack:
    "Implementation of Dynamic Stack with Dynamic List (python)"

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("The Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("The Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    "Test"
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack.peek())
    print(stack)

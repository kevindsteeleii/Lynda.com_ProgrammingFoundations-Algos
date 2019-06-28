class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

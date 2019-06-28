class Stack:
    def __init__(self):
        self.stack = list()
        self._count = 1

    def push(self, val):
        self.stack.append(val)
        self._count += 1

    def pop(self):
        self.stack.pop()
        self._count -= 1

    @property
    def count(self):
        return self._count

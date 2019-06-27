class Node:
    def add(self, node):
        target = self
        while target.tail != None:
            target = target.tail
        target.tail = node
        return node

    def __init__(self, head):
        self.head = head
        self.tail = None

# class of Node for singly linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def to_str(self):
        return self.val

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.count = 1

    def to_str(self):
        val = "Linked List: " + str(self.head.val)
        curr = self.head.get_next()
        while curr != None:
            val += " -> " + str(curr.val)
            curr = curr.get_next()
        return val

    def insert(self, data):
        last = self.head
        node = Node(data)
        while last.get_next() != None:
            last = last.get_next()
        last.set_next(node)
        self.count += 1

    def get_at(self, idx):
        if idx > self.count - 1:
            return
        else:
            i, curr = 0, self.head
            while i < idx:
                curr = curr.get_next()
                i += 1
            return curr

    def delete_at(self, idx):
        if idx > self.count:
            return
        else:
            i, curr, prev = 0, self.head, self.head
            while i < idx:
                prev = curr
                curr = curr.get_next()
                i += 1
            if idx == self.count:
                return


ex = Node(23)
links = LinkedList(23)
links.insert(12)
print(ex)
print(links.to_str())

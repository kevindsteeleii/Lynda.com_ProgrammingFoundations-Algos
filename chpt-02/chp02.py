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

    def get_count(self):
        return self.count

    def find(self, val):
        curr = self.head
        if self.head.get_val() == val:
            return self
        else:
            while val != curr.get_val():
                curr = curr.get_next()
            return curr

    def to_str(self):
        val = "Linked List: " + str(self.head.get_val())
        curr = self.head.get_next()
        while curr != None:
            val += " -> " + str(curr.get_val())
            curr = curr.get_next()
        return val

    def insert(self, data):
        last = self.head
        node = Node(data)
        while last.get_next() != None:
            last = last.get_next()
        last.set_next(node)
        self.count += 1

    def insert_at(self, node, idx):
        prev = self.head
        curr = self.head
        i = 0
        if idx > self.count - 1:
            return
        elif idx == 0:
            self.head = prev.get_next()
            prev.set_val(None)

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
        if idx > self.count - 1:
            return
        elif idx == 0:
            temp = self.head
            self.head = self.head.get_next()
            temp.set_next(None)
        else:
            i = 0
            curr = self.head
            prev = self.head
            while i < idx:
                prev = curr
                curr = curr.get_next()
                i += 1
            if idx == self.count - 1:
                prev.set_next(None)
            else:
                prev.set_next(curr.get_next())
                curr.set_next(None)


ex = Node(23)
links = LinkedList(23)
links.insert(12)
print(links.find(12).to_str())
links.insert("another one")
links.delete_at(1)
print(ex.to_str())
print(links.to_str())

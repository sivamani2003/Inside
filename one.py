class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CyclicLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def delete(self, key):
        if not self.head:
            return

        prev = None
        current = self.head

        while current:
            if current.data == key:
                if prev:
                    prev.next = current.next
                    if current == self.head:
                        self.head = current.next
                else:
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    if temp == self.head:
                        self.head = None
                    else:
                        temp.next = self.head
                return
            prev = current
            current = current.next
            if current == self.head:
                break

    def display(self):
        if not self.head:
            return

        temp = self.head
        while True:
            print(temp.data, end=' ')
            temp = temp.next
            if temp == self.head:
                break

# Example usage:
clist = CyclicLinkedList()
clist.append(1)
clist.append(2)
clist.append(3)
clist.append(4)

print("Original List:")
clist.display()
print()

clist.delete(2)

print("List after deleting 2:")
clist.display()

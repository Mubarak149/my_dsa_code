#singly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


    def __repr__(self):
        return f'{self.data}'

class doublyLinkedlist:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

# inserting a new element is in bigO(1)
    def insert(self, data):
        if self.head is None:
            newnode = Node(data)
            self.head = newnode
            self.last = newnode
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

        self.size += 1

# searching in linked list is in bigO(n)
    def search(self,data):
        node = self.head
        while node is not None:
            if node.data == data:
                return True
            else:
                node = node.next

# deletion in linked list is in bigO(n)
    def remove(self, data):
        node = self.head
        prev_node = None
        while node is not None:
            if data == node.data: #if succeed found the data to remove
                if prev_node is None: #removing first element
                    self.head = node.next
                    self.size -= 1
                    return node.data
                elif node.next is not None: #removing middile element
                    prev_node.next = node.next
                    node.next.prev = node.prev
                    self.size -= 1
                    return node.data
                else: #removing last element
                    prev_node.next = None
                    self.last = prev_node
                    node.prev = None
                    self.size -= 1
                    return node.data

            prev_node = node
            node = node.next
        return None

# printing a link list in bigO(n)
    def print_links(self,reverse):
        if reverse:
            node = self.last
            while node is not None:
                print(f'<--({node.data})-->', end='')
                node = node.prev

        else:
            node = self.head
            while node is not None:
                print(f'<--({node.data})-->',end='')
                node = node.next
        print(None)

l = doublyLinkedlist()
l.insert(7)
l.insert(8)
l.insert(9)
l.insert(10)
l.insert(12)
l.insert(14)
l.insert(21)
l.insert(30)
l.remove(7)
l.print_links(False)


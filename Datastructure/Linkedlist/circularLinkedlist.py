#circular linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


    def __repr__(self):
        return f'{self.data}'

class CircularLinkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

# inserting a new element is in bigO(1)
    def insert(self, data):
        if self.size == 0:
            newnode = Node(data)
            self.head = newnode
            self.head.next = self.head
        else:
            newnode = Node(data)
            newnode.next = self.head.next
            self.head.next = newnode
        self.size += 1

# searching in linked list is in bigO(n)
    def search(self,data):
        node = self.head
        for _ in range(self.size+1):
            if node.data == data:
                return True
            else:
                node = node.next

# deletion in linked list is in bigO(n)
    def remove(self, data):
        node = self.head
        prev_node = None
        for n in range(self.size+1):
            # looking for the data to remove whether it exist
            if data == node.data:
                #is a first element if prev_node is none
                if prev_node is None:
                    self.head = node.next
                    self.size -= 1
                    return node.data
                else:
                    prev_node.next = node.next
                    self.size -= 1
                    return node.data
            prev_node = node
            node = node.next
        return None
# printing a link list in bigO(n)
    def print_links(self):
        node = self.head
        for n in range(self.size):
            print(f'({node.data})-->',end='')
            node = node.next
        print(self.head.data)

l = CircularLinkedlist()
l.insert(7)
l.insert(8)
l.insert(9)
l.insert(10)
l.insert(12)
l.insert(14)
l.insert(21)
l.insert(30)
l.remove(7)
l.insert(23)
l.print_links()


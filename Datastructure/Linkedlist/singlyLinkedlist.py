#singly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


    def __repr__(self):
        return f'{self.data}'

class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

# inserting a new element is in bigO(1)
    def insert(self, data):
        newnode = Node(data)
        newnode.next = self.head
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

        return None

# deletion in linked list is in bigO(n)
    def remove(self, data):
        node = self.head
        prev_node = None
        while node is not None:
            if data == node.data:
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
        while node is not None:
            print(f'({node.data})-->',end='')
            node = node.next
        print(None)

l = Linkedlist()
l.insert(7)
l.insert(8)
l.insert(9)
l.insert(10)
l.insert(12)
l.insert(14)
l.insert(21)
l.insert(30)
l.print_links()


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = Tree(data)
                return True

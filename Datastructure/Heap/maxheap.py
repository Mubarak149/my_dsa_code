class MaxHeap:
    def __init__(self, datas=[]):
        self.heap = [0]
        for data in datas:
            self.push(self, data)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(-1)

    def peek(self):
        if len(self.heap)>1:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, -1)
            max = self.heap.pop()
            self.__bubbleDown(1)

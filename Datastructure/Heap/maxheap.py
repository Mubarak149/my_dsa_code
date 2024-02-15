class MaxHeap:
    def __init__(self, datas=[]):
        self.heap = [0]
        for data in datas:
            self.push(data)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

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
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max
    def __swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, parentIndex):
        leftChild = parentIndex * 2
        rightChild = leftChild + 1
        largestChild = parentIndex
# check if it's a valid index and largest is less than it's left child
        if len(self.heap) > leftChild and self.heap[largestChild] < self.heap[leftChild]:
            largestChild = leftChild
        if len(self.heap) > rightChild and self.heap[largestChild] < rightChild:
            largestChild = rightChild
        if largestChild != parentIndex:
            self.__swap(largestChild, parentIndex) # largechild = parent while parent = largechild
            self.__bubbleDown(largestChild) # then we bubble the largechild(he is the parent now)

    def accessParent(self,data):
        childs = []
        if data in self.heap:
            parentChild = self.heap.index(data)
            leftChildIndex = parentChild * 2
            rightChildIndex = parentChild * 2 + 1
            if len(self.heap) > rightChildIndex:
                leftChildData = self.heap[leftChildIndex]
                rightChildData = self.heap[rightChildIndex]
                childs = [leftChildData, rightChildData]
            elif len(self.heap) >= leftChildIndex:
                leftChildData = self.heap[leftChildIndex]
                childs.append(leftChildData)
# we have the data but does not have a child element
            else:
                return []
            return childs
# if we cant find the data
        return None


# Test code
m = MaxHeap([10,11,12,13,14,15,16,17,18,19,20])
print(m.peek())
print(m.heap)
print(m.accessParent(16))


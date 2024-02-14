class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.front = self.rear = -1


    def is_empty(self):
        return self.front == -1

    def is_full(self):
# last index = 19 self.rear contain our last index
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, data):
        if self.is_full():
            print('Queue is full. cannaot enqueue')
            return
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print('Queue is full. Cannot dequeue')
            return
# replacing the data with None value and shift the front pointer
        dequeued_data = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        print(f'Dequeued: {dequeued_data}')
        return dequeued_data

    def display(self):
        if self.is_empty():
            print('Queue is empty')
            return
        current =  self.front
        print('Circular queue')
        while True:
            print(self.queue[current], end=' ')
            if current == self.rear:
                break
            current = (current + 1) % self.capacity
            print()


cq = CircularQueue(20)
cq.enqueue(12)
cq.enqueue(13)
cq.enqueue(14)
cq.enqueue(16)
cq.enqueue(17)
cq.enqueue(19)
cq.enqueue(20)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()

cq.display()
cq = CircularQueue(20)
class PriorityQueue:

    def __init__(self,items=[]):
# if pass a list make it the queue
        self.queue = [] if len(items) == 0 else items

    def enque(self, data):
        self.queue.append(data)

    def dequeing(self):
# it is O(1) to pop the first element of a Python list
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def __repr__(self):
        return str(self.queue)





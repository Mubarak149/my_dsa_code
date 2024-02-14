class Stack:
    def __init__(self, datas=[]):
# if pass a list make it the stack
        self.__stack = [] if len(datas) == 0 else datas

    def push(self,data):
        self.__stack.append(data)

    def size(self):
        return len(self.__stack)


my_stack = Stack()
my_stack.push(12)
my_stack.push(92)
my_stack.push(42)
my_stack.push(52)
my_stack.push(22)
print(my_stack.size())
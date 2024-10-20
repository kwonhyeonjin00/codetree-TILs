class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0

    def top(self):
        return self.items[-1]

n = int(input())

stack = Stack()

for i in range(n):
    x = input().split()

    if x[0] == 'push':
        stack.push(int(x[1]))
    elif x[0] == 'pop':
        print(stack.pop())
    elif x[0] == 'size':
        print(stack.size())
    elif x[0] == 'empty':
        print(stack.empty())
    elif x[0] == 'top':
        print(stack.top())
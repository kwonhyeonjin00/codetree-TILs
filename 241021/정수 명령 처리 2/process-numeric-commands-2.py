from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
                
    def push(self, item):
        self.dq.append(item)
                
    def empty(self):
        return 1 if not self.dq else 0
                
    def size(self):
        return len(self.dq)
        
    def pop(self):
        return self.dq.popleft()
                
    def front(self):
        return self.dq[0]

n = int(input())

q = Queue()

for i in range(n):
    x = input().split()

    if x[0] == 'push':
        q.push(int(x[1]))
    elif x[0] == 'pop':
        print(q.pop())
    elif x[0] == 'size':
        print(q.size())
    elif x[0] == 'empty':
        print(q.empty())
    elif x[0] == 'front':
        print(q.front())
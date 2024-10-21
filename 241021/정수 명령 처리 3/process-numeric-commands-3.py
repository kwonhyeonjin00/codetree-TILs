from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push_front(self, item):
        self.dq.appendleft(item)
                
    def push_back(self, item):
        self.dq.append(item)

    def pop_front(self):
        return self.dq.popleft()

    def pop_back(self):
        return self.dq.pop()

    def size(self):
        return len(self.dq)
                
    def empty(self):
        return 1 if not self.dq else 0
                
    def front(self):
        return self.dq[0]
    
    def back(self):
        return self.dq[-1]

n = int(input())

q = Queue()

for i in range(n):
    x = input().split()

    if x[0] == 'push_front':
        q.push_front(int(x[1]))
    elif x[0] == 'push_back':
        q.push_back(int(x[1]))
    elif x[0] == 'pop_front':
        print(q.pop_front())
    elif x[0] == 'pop_back':
        print(q.pop_back())
    elif x[0] == 'size':
        print(q.size())
    elif x[0] == 'empty':
        print(q.empty())
    elif x[0] == 'front':
        print(q.front())
    elif x[0] == 'back':
        print(q.back())
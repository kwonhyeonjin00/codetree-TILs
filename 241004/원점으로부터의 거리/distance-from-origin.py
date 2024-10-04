class Dot:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number

n = int(input())

dot = []
for i in range(n):
    x, y = map(int, input().split())
    dot.append(Dot(x, y, i+1))

dot.sort(key=lambda k: (abs(k.x) + abs(k.y), k.number))

for x in dot:
    print(f'{x.number}')
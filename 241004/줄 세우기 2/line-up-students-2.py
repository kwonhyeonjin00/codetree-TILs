class People:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())

people = []
for i in range(n):
    height, weight = map(int, input().split())
    people.append(People(height, weight, i+1))

people.sort(key=lambda x: (x.height, -x.weight, x.number))

for x in people:
    print(f'{x.height} {x.weight} {x.number}')
class People:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

people = []
for i in range(n):
    name, height, weight = input().split()
    people.append(People(name, height, weight))

people.sort(key=lambda x: x.height)

for x in people:
    print(f'{x.name} {x.height} {x.weight}')
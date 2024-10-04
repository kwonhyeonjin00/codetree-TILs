class People:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = []
for i in range(5):
    name, height, weight = map(str, input().split())
    height, weight = int(height), float(weight)
    people.append(People(name, height, weight))

people.sort(key=lambda x: x.name)

print("name")
for x in people:
    print(f'{x.name} {x.height} {x.weight}')

print("\nheight")
people.sort(key=lambda x: -x.height)

for x in people:
    print(f'{x.name} {x.height} {x.weight}')
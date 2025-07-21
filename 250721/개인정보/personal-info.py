N = 5
name = []
height = []
weight = []

for _ in range(N):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
class People:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

people = []

for i in range(N):
    people.append(People(name[i], height[i], weight[i]))

people.sort(key=lambda x: x.name)
print("name")
for t in people:
    print(t.name, t.height, t.weight)

print()

people.sort(key=lambda x: -x.height)
print("height")
for t in people:
    print(t.name, t.height, t.weight)
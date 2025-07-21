n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
class People:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

people = []

for i in range(n):
    people.append(People(name[i], height[i], weight[i]))

people.sort(key=lambda x: (x.height, -x.weight))

for t in people:
    print(t.name, t.height, t.weight)
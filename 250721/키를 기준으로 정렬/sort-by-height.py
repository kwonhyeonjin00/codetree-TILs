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
class Member:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

members = []
for i in range(n):
    members.append(Member(name[i], height[i], weight[i]))

members.sort(key=lambda x: x.height)

for member in members:
    print(member.name, member.height, member.weight)
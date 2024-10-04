class People:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

n = int(input())

names = []

people = []
for i in range(n):
    name, addr, city = input().split()
    people.append(People(name, addr, city))
    names.append([name, i])

names.sort()
idx = names[-1][1]

print(f'name {people[idx].name}')
print(f'addr {people[idx].addr}')
print(f'city {people[idx].city}')
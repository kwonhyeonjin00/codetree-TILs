n = int(input())
names = []
street_address = []
regions = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    names.append(n_i)
    street_address.append(s_i)
    regions.append(r_i)

# Please write your code here.
class Member:
    def __init__(self, name, street_address, region):
        self.name = name
        self.street_address = street_address
        self.region = region

member = []

for i in range(n):
    member.append(Member(names[i], street_address[i], regions[i]))

l_p = 0

for i in range(1, n):
    if member[l_p].name < member[i].name:
        l_p = i

print(f"name {member[l_p].name}")
print(f"addr {member[l_p].street_address}")
print(f"city {member[l_p].region}")
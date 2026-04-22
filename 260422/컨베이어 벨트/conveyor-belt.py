n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.

for i in range(t):
    temp = u.pop()
    d.insert(0, temp)

    temp = d.pop()
    u.insert(0, temp)

for x in u:
    print(x, end=' ')
print()
for x in d:
    print(x, end=' ')
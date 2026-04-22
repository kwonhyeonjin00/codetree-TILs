n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
for i in range(t):
    temp = l.pop()
    r.insert(0, temp)

    temp = r.pop()
    d.insert(0, temp)

    temp = d.pop()
    l.insert(0, temp)

for x in l:
    print(x, end=' ')
print()
for x in r:
    print(x, end=' ')
print()
for x in d:
    print(x, end=' ')
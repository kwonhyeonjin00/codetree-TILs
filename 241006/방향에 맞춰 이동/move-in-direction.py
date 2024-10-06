n = int(input())
x, y = 0, 0

for i in range(n):
    d, s = input().split()
    s = int(s)

    if d == 'N':
        x, y = x, y + s
    elif d == 'S':
        x, y = x, y - s
    elif d == 'E':
        x, y = x + s, y
    elif d == 'W':
        x, y = x - s, y

print(x, y)
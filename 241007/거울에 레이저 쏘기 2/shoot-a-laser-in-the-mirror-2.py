def check(x, y):
    return 0 <= x < n and 0 <= y < n

n = int(input())

dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]

arr = []
for i in range(n):
    a = list(input())
    arr.append(a)

k = int(input())

t = (k-1) // n
s = (k-1) % n

if t == 0:
    x, y, d = 0, s, 0
elif t == 1:
    x, y, d = s, n - 1, 2
elif t == 2:
    x, y, d = n - 1, n - s - 1, 1
elif t == 3:
    x, y, d = n - s - 1, 0, 3

cnt = 0

while True:
    if check(x, y) == False:
        print(cnt)
        break

    if arr[x][y] == '/':
        d = 3 - d
    elif arr[x][y] == '\\':
        d = (d + 2) % 4 
    cnt += 1

    x, y = x + dxs[d], y + dys[d]
    if d == 0 or d == 2:
        d += 1
    elif d == 1 or d == 3:
        d -= 1
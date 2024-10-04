def check(arr):
    for i in range(2000):
        for j in range(2000):
            if arr[i][j] == 1:
                return i, j

arr = [[0 for _ in range(2000)] for _ in range(2000)]

x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1+1000, y1+1000, x2+1000, y2+1000

for j in range(x1, x2+1):
    for k in range(y1, y2+1):
        arr[j][k] = 1

x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1+1000, y1+1000, x2+1000, y2+1000

for j in range(x1, x2+1):
    for k in range(y1, y2+1):
        arr[j][k] = 0

xt1, yt1 = check(arr)

for i in range(2000):
    for j in range(2000):
        if arr[i][j] == 1:
            xt2, yt2 = i, j

print((xt2 - xt1) * (yt2 - yt1))
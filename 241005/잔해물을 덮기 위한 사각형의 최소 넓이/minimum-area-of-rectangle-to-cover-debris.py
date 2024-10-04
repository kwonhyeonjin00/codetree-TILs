def check(arr):
    for i in range(2000):
        for j in range(2000):
            if arr[i][j] == 1:
                return i, j

def check1(arr):
    for i in range(1999, -1, -1):
        for j in range(1999, -1, -1):
            if arr[i][j] == 1:
                return i, j

arr = [[0 for _ in range(2000)] for _ in range(2000)]

x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1+1000, y1+1000, x2+1000, y2+1000

for j in range(x1, x2):
    for k in range(y1, y2):
        arr[j][k] = 1

x3, y3, x4, y4 = map(int, input().split())
x3, y3, x4, y4 = x3+1000, y3+1000, x4+1000, y4+1000

for j in range(x1, x2):
    for k in range(y1, y2):
        if x3 <= j < x4 and y3 <= k < y4:
            arr[j][k] = 0
            
xt1, yt1 = check(arr)
xt2, yt2 = check1(arr)

print((xt2 - xt1 + 1) * (yt2 - yt1 + 1))
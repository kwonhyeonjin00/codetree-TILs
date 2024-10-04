arr = [[0 for _ in range(2000)] for _ in range(2000)]

for i in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1+1000, y1+1000, x2+1000, y2+1000

    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[j][k] = 1

x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1+1000, y1+1000, x2+1000, y2+1000

for j in range(x1, x2):
    for k in range(y1, y2):
        arr[j][k] = 0

cnt = 0

for i in arr:
    cnt += i.count(1)

print(cnt)
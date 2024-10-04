n = int(input())

arr = [[0 for _ in range(200)] for _ in range(200)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1+100, y1+100, x2+100, y2+100

    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[j][k] += 1

cnt = 0

for i in range(n):
    for j in arr:
        cnt += j.count(i+1)

print(cnt)
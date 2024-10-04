n = int(input())

arr = [[0 for _ in range(200)] for _ in range(200)]

for i in range(n):
    x1, y1 = map(int, input().split())
    x1, y1 = x1+100, y1+100

    for j in range(x1, x1+8):
        for k in range(y1, y1+8):
            arr[j][k] = 1

cnt = 0

for i in arr:
    cnt += i.count(1)
    
print(cnt)
n = int(input())

arr = [0 for _ in range(2001)]

idx = 1000

for i in range(n):
    x, t = input().split()
    x = int(x)
    if t == 'R':
        for j in range(idx, idx+x):
            arr[j] += 1
        idx += x
    elif t == 'L':
        for j in range(idx, idx-x, -1):
            arr[j] += 1
        idx -= x 

cnt = 0
for i in arr:
    if i >= 2:
        cnt += 1

print(cnt)
n = int(input())
arr = [0 for _ in range(n*10+1)]

idx = n*5

for i in range(n):
    x, t = input().split()
    x = int(x)
    if t == 'R':
        for j in range(idx, idx+x):
            if arr[j] == 5:
                continue
            else:
                arr[j] += 1
        idx += x
    elif t == 'L':
        for j in range(idx-1, idx-x-1, -1):
            if arr[j] == 3:
                arr[j] = 5
            elif arr[j] == 5:
                continue
            elif arr[j] == 0:
                arr[j] = 2
            else:
                arr[j] += 1
        idx -= x 

cnt_w = 0
cnt_b = 0
cnt_g = 0

for i in arr:
    if i == 2 or i == 4:
        cnt_w += 1
    elif i == 1 or i == 3:
        cnt_b += 1
    elif i == 5:
        cnt_g += 1

print(cnt_w, cnt_b, cnt_g)
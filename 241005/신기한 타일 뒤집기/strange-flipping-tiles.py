n = int(input())
arr = ['0' for _ in range(n*198+1)]

idx = n*99

for i in range(n):
    x, t = input().split()
    x = int(x)
    if t == 'R':
        for j in range(idx, idx+x):
            arr[j] = 'b'

        idx += x-1
    elif t == 'L':
        for j in range(idx, idx-x, -1): 
            arr[j] = 'w'
        idx -= x-1

cnt_w = 0
cnt_b = 0

for i in arr:
    if i == 'w':
        cnt_w += 1
    elif i == 'b':
        cnt_b += 1

print(cnt_w, cnt_b)
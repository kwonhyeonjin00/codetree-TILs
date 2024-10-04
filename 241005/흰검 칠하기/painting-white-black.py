n = int(input())
arr = [[0, 0, '0'] for _ in range(n*198+1)]

idx = n*99

for i in range(n):
    x, t = input().split()
    x = int(x)
    if t == 'R':
        for j in range(idx, idx+x):
            arr[j][1] += 1
            arr[j][2] = 'b'

        idx += x-1
    elif t == 'L':
        for j in range(idx, idx-x, -1): 
            arr[j][0] += 1
            arr[j][2] = 'w'
        idx -= x-1

cnt_w = 0
cnt_b = 0
cnt_g = 0

for i in arr:
    if i[0] >= 2 and i[1] >= 2:
        cnt_g += 1
    elif i[2] == 'w':
        cnt_w += 1
    elif i[2] == 'b':
        cnt_b += 1

print(cnt_w, cnt_b, cnt_g)
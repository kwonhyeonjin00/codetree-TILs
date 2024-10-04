n = int(input())
arr = [[0, '0'] for _ in range(n*2+1)]

idx = n

for i in range(n):
    x, t = input().split()
    x = int(x)
    if t == 'R':
        for j in range(idx+1, idx+x+1):
            if arr[j][1] == 'g':
                continue
            elif arr[j][0] == 3:
                arr[j][1] = 'g'
            
            arr[j][0] += 1
            arr[j][1] = 'b'

        idx += x
    elif t == 'L':
        for j in range(idx, idx-x, -1):
            if arr[j][1] == 'g':
                continue
            elif arr[j][0] == 3:
                arr[j][1] = 'g'
            
            arr[j][0] += 1
            arr[j][1] = 'w'
        idx -= x 
    print(arr)
cnt_w = 0
cnt_b = 0
cnt_g = 0

for i in arr:
    if i[1] == 'w':
        cnt_w += 1
    elif i[1] == 'b':
        cnt_b += 1
    elif i[1] == 'g':
        cnt_g += 1

print(cnt_w, cnt_b, cnt_g)
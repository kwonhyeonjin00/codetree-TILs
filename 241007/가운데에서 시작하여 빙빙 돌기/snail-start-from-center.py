def check(x, y):
    return 0 <= x < n and 0 <= y < n

def number(x, y, n):
    global cnt
    if n % 2 == 1:
        for i in range(n):
            x, y = x + dxs[0], y + dys[0]
            if check(x, y) == False:
                x, y = x - dxs[0], y - dys[0]
                break
            arr[x][y] = cnt
            cnt += 1
        for j in range(n):
            x, y = x + dxs[1], y + dys[1]
            if check(x, y) == False:
                x, y = x - dxs[1], y - dys[1]
                break
            arr[x][y] = cnt
            cnt += 1
    elif n % 2 == 0:
        for i in range(n):
            x, y = x + dxs[2], y + dys[2]
            if check(x, y) == False:
                x, y = x - dxs[2], y - dys[2]
                break
            arr[x][y] = cnt
            cnt += 1
        for j in range(n):
            x, y = x + dxs[3], y + dys[3]
            if check(x, y) == False:
                x, y = x - dxs[3], y - dys[3]
                break
            arr[x][y] = cnt
            cnt += 1
    return x, y
n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]

x, y = (n-1) // 2, (n-1) // 2

cnt = 1
arr[x][y] = cnt
cnt += 1
for i in range(1, n):
    x, y = number(x, y, i)

for j in range(n-1):
    
    x, y = x + dxs[0], y + dys[0]
    if check(x, y) == False:
        x, y = x - dxs[0], y - dys[0]
        break
    arr[x][y] = cnt
    cnt += 1

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()
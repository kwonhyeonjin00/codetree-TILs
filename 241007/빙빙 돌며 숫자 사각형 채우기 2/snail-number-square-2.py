n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
x, y = 0, 0
dir_num = 0

arr[x][y] = 1

for i in range(2, n * m + 1):
    x, y = x + dxs[dir_num], y + dys[dir_num]
    if in_range(x, y) == False or arr[x][y] != 0:
        x, y = x - dxs[dir_num], y - dys[dir_num]
        dir_num = (dir_num + 1) % 4
        x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
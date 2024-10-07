n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
dir_num = 0

char = 65

arr[x][y] = chr(char)

for i in range(1, n * m):
    x, y = x + dxs[dir_num], y + dys[dir_num]
    if in_range(x, y) == False or arr[x][y] != 0:
        x, y = x - dxs[dir_num], y - dys[dir_num]
        dir_num = (dir_num + 1) % 4
        x, y = x + dxs[dir_num], y + dys[dir_num]
    if char + i == 91:
        char -= 26
    arr[x][y] = chr(char + i)

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
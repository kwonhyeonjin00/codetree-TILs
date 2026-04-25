n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
r, c = r - 1, c - 1
x = grid[r][c]

if x >= 1:
    grid[r][c] = 0

    dx, dy = r, c
    # 위 제거
    for i in range(x - 1):
        dx -= 1
        if dx >= 0:
            grid[dx][dy] = 0
        else:
            break

    dx, dy = r, c
    # 오른쪽 제거
    for i in range(x - 1):
        dy += 1
        if dy < n:
            grid[dx][dy] = 0
        else:
            break

    dx, dy = r, c
    # 왼쪽 제거
    for i in range(x - 1):
        dy -= 1
        if dy >= 0:
            grid[dx][dy] = 0
        else:
            break

    dx, dy = r, c
    # 아래 제거
    for i in range(x - 1):
        dx += 1
        if dx < n:
            grid[dx][dy] = 0
        else:
            break
        
temp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    nx, ny = n - 1, i
    for j in range(n - 1, -1, -1):
        if grid[j][i] != 0:
            temp[nx][ny] = grid[j][i]
            nx -= 1

for row in temp:
    print(*row)
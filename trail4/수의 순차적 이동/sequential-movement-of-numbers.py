n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 북 북동 동 동남 남 남서 서 북서 
dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

pos_list = [0] * (n ** 2 + 1)

# 1~n*n까지 순서대로 위치 저장
for i in range(n):
    for j in range(n):
        pos_list[grid[i][j]] = [i, j]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def check(x, y):
    max_val = 0
    temp_x, temp_y = x, y

    for i in range(8):
        nx, ny = x + dxs[i], y + dys[i]
        if in_range(nx, ny):
            if max_val < grid[nx][ny]:
                max_val = grid[nx][ny]
                temp_x, temp_y = nx, ny

    return temp_x, temp_y

for i in range(m):
    for j in range(1, n ** 2 + 1):
        
        x, y = pos_list[j]
        nx, ny = check(x, y)

        grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
        pos_list[grid[x][y]], pos_list[grid[nx][ny]] = pos_list[grid[nx][ny]], pos_list[grid[x][y]]

for row in grid:
    print(*row)

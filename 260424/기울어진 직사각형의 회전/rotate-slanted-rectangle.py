n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

# Please write your code here.

dx, dy = r - 1, c - 1

if dir == 0:
    temp = grid[dx][dy]

    for i in range(1, m4 + 1):
        dx, dy = dx - 1, dy - 1
        grid[dx + 1][dy + 1] = grid[dx][dy]

    for i in range(1, m3 + 1):
        dx, dy = dx - 1, dy + 1
        grid[dx + 1][dy - 1] = grid[dx][dy]

    for i in range(1, m2 + 1):
        dx, dy = dx + 1, dy + 1
        grid[dx - 1][dy - 1] = grid[dx][dy]

    for i in range(1, m1 + 1):
        dx, dy = dx + 1, dy - 1
        grid[dx - 1][dy + 1] = grid[dx][dy]

    grid[dx - 1][dy + 1] = temp

elif dir == 1:
    temp = grid[dx][dy]

    for i in range(1, m1 + 1):
        dx, dy = dx - 1, dy + 1
        grid[dx + 1][dy - 1] = grid[dx][dy]

    for i in range(1, m2 + 1):
        dx, dy = dx - 1, dy - 1
        grid[dx + 1][dy + 1] = grid[dx][dy]

    for i in range(1, m3 + 1):
        dx, dy = dx + 1, dy - 1
        grid[dx - 1][dy + 1] = grid[dx][dy]

    for i in range(1, m4 + 1):
        dx, dy = dx + 1, dy + 1
        grid[dx - 1][dy - 1] = grid[dx][dy]

    grid[dx - 1][dy - 1] = temp

for row in grid:
    print(*row)
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]

for c in commands:
    r = -1
    c -= 1

    for i in range(n):
        if grid[i][c] > 0:
            r = i
            break
    if r == -1:
        continue

    x = grid[r][c]
    
    grid[r][c] = 0

    for i in range(n):
        for j in range(n):
           if (i == r and abs(j - c) < x) or (j == c and abs(i - r) < x):
            grid[i][j] = 0
    
    for col in range(n):
        temp = []
        for row in range(n):
            if grid[row][col] > 0:
                temp.append(grid[row][col])

        new = [0] * (n - len(temp)) + temp
        for row in range(n):
            grid[row][col] = new[row]

for row in grid:
    print(*row)
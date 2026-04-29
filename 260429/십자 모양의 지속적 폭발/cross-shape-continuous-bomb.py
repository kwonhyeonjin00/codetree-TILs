n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]

for c in commands:
    c -= 1

    for i in range(n):
        if grid[i][c] > 0:
            r = i
            break
    
    x = grid[r][c]
    
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
    
    ans = list(map(list, zip(*grid[::-1])))

    for i in range(n):
        ans[i] = [x for x in ans[i] if x > 0]
        while len(ans[i]) < n:
            ans[i].append(0)

    ans = [row[::-1] for row in ans]
    ans = list(map(list, zip(*ans)))


for row in ans:
    print(*row)
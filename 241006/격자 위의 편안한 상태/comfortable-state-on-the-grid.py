n, m = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

def check(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 1:
                cnt += 1
    return cnt

for i in range(m):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

    cnt = check(r-1, c-1)

    if cnt == 3:
        print(1)
    else:
        print(0)
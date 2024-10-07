def check(x, y):
    return 0 <= x < n and 0 <= y < n

n, t = map(int, input().split())
s = list(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = (n-1) // 2, (n-1) // 2
d = 3
cnt = [arr[x][y]]

for elem in s:
    if elem == 'R':
        d = (d+1) % 4
    elif elem == 'L':
        d = (d-1) % 4
    elif elem == 'F':
        x, y = x + dxs[d], y + dys[d]
        if check(x, y) == False:
            x, y = x - dxs[d], y - dys[d]
        else:
            cnt.append(arr[x][y])

print(sum(cnt))
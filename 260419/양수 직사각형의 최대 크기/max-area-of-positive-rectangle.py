n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
cnt_list = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):

        if grid[i][j] > 0:
            if i == 0:
                cnt_list[i][j] = 1
            else:
                cnt_list[i][j] = cnt_list[i - 1][j] + 1

res = [0]

for i in range(n):
    for j in range(m):
        size = 1
        h = cnt_list[i][j]
        res.append(size * h)

        for k in range(j + 1, m):
            if cnt_list[i][k] > 0:
                h = min(h, cnt_list[i][k])
                size += 1
            else:
                break
            res.append(h * size)

print(max(res))
            
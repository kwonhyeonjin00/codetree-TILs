n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 상 우 하 좌
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
# 0 = 빔 1 = / 2 = \

def in_range(dx, dy):
    if (dx < 0 or dx >= n) or (dy < 0 or dy >= n):
        return False
    return True

def check(dx, dy, d):
    time = 1
    while in_range(dx, dy) == True:
        if grid[dx][dy] == 1:
            d ^= 1
        elif grid[dx][dy] == 2:
            d = 3 - d

        dx += dxs[d]
        dy += dys[d]
        time += 1


    return time

max_time = -1

for w in range(n):
    time = check(n-1, w, 0)
    max_time = max(max_time, time)

for x in range(n):
    time = check(x, 0, 1)
    max_time = max(max_time, time)

for y in range(n):
    time = check(0, y, 2)
    max_time = max(max_time, time)

for z in range(n):
    time = check(z, n-1, 3)
    max_time = max(max_time, time)

print(max_time)
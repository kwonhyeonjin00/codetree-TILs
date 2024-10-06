n = int(input())

def in_range(x, y):
    global n
    return 0 <= x and x < n and 0 <= y and y < n

arr = []

for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
cnt_3 = 0


for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if in_range(nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            cnt_3 += 1

print(cnt_3)
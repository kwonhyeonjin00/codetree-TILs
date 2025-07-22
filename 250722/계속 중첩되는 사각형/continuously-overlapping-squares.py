n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
check = [[0 for _ in range(200)] for _ in range(200)]
OFF = 100

def paint_red(d_x1, d_y1, d_x2, d_y2):
    for i in range(d_x1, d_x2):
        for j in range(d_y1, d_y2):
            check[i][j] = 1

def paint_blue(d_x1, d_y1, d_x2, d_y2):
    for i in range(d_x1, d_x2):
        for j in range(d_y1, d_y2):
            check[i][j] = 2

t = n % 2

for i in range(0, n - t, 2):
    paint_red(x1[i] + 100, y1[i] + 100, x2[i] + 100, y2[i] + 100)
    paint_blue(x1[i + 1] + 100, y1[i + 1] + 100, x2[i + 1] + 100, y2[i + 1] + 100)

if t == 1:
    paint_red(x1[n -1], y1[n - 1], x2[n - 1], y2[n - 1])

cnt = 0

for i in range(200):
    for j in range(200):
        if check[i][j] == 2:
            cnt += 1

print(cnt)
x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
stack = [[0 for _ in range(2000)] for _ in range(2000)]

t1 = x1[0] + 1000
s1 = y1[0] + 1000
t2 = x2[0] + 1000
s2 = y2[0] + 1000
for j in range(t1, t2):
    for k in range(s1, s2):
        stack[j][k] = 1

t1 = x1[1] + 1000
s1 = y1[1] + 1000
t2 = x2[1] + 1000
s2 = y2[1] + 1000
for j in range(t1, t2):
    for k in range(s1, s2):
        stack[j][k] = 0

max_x1, max_y1 = 0, 0
max_x2, max_y2 = 0, 0
min_x1, min_y1 = 0, 0
min_x2, min_y2 = 0, 0

for i in range(2000):
    if min_x1 != 0 and min_y1 != 0:
        break
    for j in range(2000):
        if stack[i][j] == 1:
            min_x1, min_y1 = i, j
            break

for i in range(2000):
    if min_x2 != 0 and min_y2 != 0:
        break
    for j in range(2000):
        if stack[j][i] == 1:
            min_x2, min_y2 = j, i
            break

for i in range(1999, 0, -1):
    if max_x1 != 0 and max_y1 != 0:
        break
    for j in range(1999, 0, -1):
        if stack[i][j] == 1:
            max_x1, max_y1 = i + 1, j + 1
            break

for i in range(1999, 0, -1):
    if max_x2 != 0 and max_y2 != 0:
        break
    for j in range(1999, 0, -1):
        if stack[j][i] == 1:
            max_x2, max_y2 = j + 1, i + 1
            break

ans_x1 = min(min_x1, min_x2)
ans_y1 = min(min_y1, min_y2)
ans_x2 = max(max_x1, max_x2)
ans_y2 = max(max_y1, max_y2)

print((ans_x2 - ans_x1) * (ans_y2 - ans_y1))
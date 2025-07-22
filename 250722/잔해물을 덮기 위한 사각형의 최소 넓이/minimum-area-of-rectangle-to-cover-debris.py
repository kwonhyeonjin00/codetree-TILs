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

cnt_x = []
cnt_y = []

for i in stack:
    cnt_x.append(i.count(1))

for i in range(2000):
    cnt = 0
    for j in range(2000):
        if stack[j][i] == 1:
            cnt += 1
    cnt_y.append(cnt)

print(max(cnt_x) * max(cnt_y))
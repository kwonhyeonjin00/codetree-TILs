x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
stack = [[0 for _ in range(2000)] for _ in range(2000)]

for i in range(2):
    t1 = x1[i] + 1000
    s1 = y1[i] + 1000
    t2 = x2[i] + 1000
    s2 = y2[i] + 1000
    for j in range(t1, t2):
        for k in range(s1, s2):
            stack[j][k] = 1


t1 = x1[2] + 1000
s1 = y1[2] + 1000
t2 = x2[2] + 1000
s2 = y2[2] + 1000
for j in range(t1, t2):
    for k in range(s1, s2):
        stack[j][k] = 0

cnt = 0

for x1 in stack:
    for x2 in x1:
        if x2 == 1:
            cnt += 1

print(cnt)
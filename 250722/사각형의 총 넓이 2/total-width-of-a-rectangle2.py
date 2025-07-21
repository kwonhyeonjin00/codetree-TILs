n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
stack = [[0 for _ in range(200)] for _ in range(200)]

for i in range(n):
    t1 = x1[i] + 100
    s1 = y1[i] + 100
    t2 = x2[i] + 100
    s2 = y2[i] + 100
    for j in range(t1, t2):
        for k in range(s1, s2):
            stack[j][k] = 1

cnt = 0

for x1 in stack:
    for x2 in x1:
        if x2 == 1:
            cnt += 1

print(cnt)
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
stack = [[0 for _ in range(200)] for _ in range(200)]

for i in range(n):
    t = x[i] + 100
    s = y[i] + 100
    for j in range(t, t + 8):
        for k in range(s, s + 8):
            stack[j][k] = 1

cnt = 0

for x1 in stack:
    for x2 in x1:
        if x2 == 1:
            cnt += 1

print(cnt)
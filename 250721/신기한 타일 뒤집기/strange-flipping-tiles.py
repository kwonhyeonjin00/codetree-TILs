n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
stack = ['a' for _ in range(200000)]

pos = 100000

for i in range(n):
    if dir[i] == 'L':
        stack[pos] = 'w'
        for j in range(x[i] - 1):
            pos -= 1
            stack[pos] = 'w'

    elif dir[i] == 'R':
        stack[pos] = 'b'
        for j in range(x[i] - 1):
            pos += 1
            stack[pos] = 'b'

cnt_w, cnt_b = 0, 0

for k in stack:
    if k == 'w':
        cnt_w += 1
    elif k == 'b':
        cnt_b += 1

print(cnt_w, cnt_b)
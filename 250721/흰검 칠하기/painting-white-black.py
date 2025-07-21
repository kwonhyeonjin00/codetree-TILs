n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
stack = [[0, 0, 'a'] for _ in range(200000)]

pos = 100000

for i in range(n):
    if dir[i] == 'L':
        stack[pos][0] += 1
        stack[pos][2] = 'w'
        for j in range(x[i] - 1):
            pos -= 1
            stack[pos][0] += 1
            stack[pos][2] = 'w'

    elif dir[i] == 'R':
        stack[pos][1] += 1
        stack[pos][2] = 'b'
        for j in range(x[i] - 1):
            pos += 1
            stack[pos][1] += 1
            stack[pos][2] = 'b'

cnt_w, cnt_b, cnt_g = 0, 0, 0

for k in stack:
    if k[0] >= 2 and k[1] >= 2:
        cnt_g += 1
    elif k[2] == 'w':
        cnt_w += 1
    elif k[2] == 'b':
        cnt_b += 1

print(cnt_w, cnt_b, cnt_g)
n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
stack = [0 for _ in range(20)]

pos = 10

for i in range(n):
    if dir[i] == 'R':
        pos -= 1
    else:
        pos += 1
    for j in range(x[i]):     
        if dir[i] == 'R':
            pos += 1
            if stack[pos] == 0:
                stack[pos] = 1
            elif stack[pos] == 1:
                stack[pos] = 100 
            elif stack[pos] == 10:
                stack[pos] = 113
            elif stack[pos] == 11:
                stack[pos] = 110
            elif stack[pos] == 101:
                stack[pos] = 111
            elif stack[pos] == 112:
                stack[pos] = 110
            elif stack[pos] == 113:
                stack[pos] = 110
            elif stack[pos] == 111:
                stack[pos] = 1000
        
        elif dir[i] == 'L':
            pos -= 1
            if stack[pos] == 0:
                stack[pos] = 10
            elif stack[pos] == 1:
                stack[pos] = 112
            elif stack[pos] == 10:
                stack[pos] = 101
            elif stack[pos] == 11:
                stack[pos] = 111
            elif stack[pos] == 100:
                stack[pos] = 110
            elif stack[pos] == 112:
                stack[pos] = 111
            elif stack[pos] == 113:
                stack[pos] = 111
            elif stack[pos] == 110:
                stack[pos] = 1000

cnt_b, cnt_w, cnt_g = 0, 0, 0
cnt_b += stack.count(1)
cnt_b += stack.count(100)
cnt_b += stack.count(110)
cnt_b += stack.count(113)

cnt_w += stack.count(10)
cnt_w += stack.count(101)
cnt_w += stack.count(111)
cnt_w += stack.count(112)

cnt_g += stack.count(1000)

print(cnt_w, cnt_b, cnt_g)
n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
stack = [0 for _ in range(1000000)]

pos = 50000

for i in range(n):
    if dir[i] == 'R':
        pos -= 1
    else:
        pos += 1
    for j in range(x[i]):     
        if dir[i] == 'R':
            pos += 1
            if stack[pos] == 0:
                stack[pos] = 2
            elif stack[pos] == 1:
                stack[pos] = 3 
            elif stack[pos] == 4:
                stack[pos] = 6
            elif stack[pos] == 5:
                stack[pos] = 7
        
        elif dir[i] == 'L':
            pos -= 1
            if stack[pos] == 0:
                stack[pos] = 1
            elif stack[pos] == 2:
                stack[pos] = 4
            elif stack[pos] == 3:
                stack[pos] = 5
            elif stack[pos] == 6:
                stack[pos] = 7

cnt_b, cnt_w, cnt_g = 0, 0, 0
cnt_b += stack.count(2)
cnt_b += stack.count(3)
cnt_b += stack.count(6)

cnt_w += stack.count(1)
cnt_w += stack.count(4)
cnt_w += stack.count(5)

cnt_g += stack.count(7)

print(cnt_w, cnt_b, cnt_g)
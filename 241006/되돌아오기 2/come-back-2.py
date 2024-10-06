s = list(input())
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

dir_num = 3
time = 0
check = 0

for elem in s:
    if elem == 'R':
        dir_num = (dir_num + 1) % 4
    elif elem == 'L':
        dir_num = (dir_num - 1) % 4
    elif elem == 'F':
        x, y = x + dx[dir_num], y + dy[dir_num]
    time += 1
    if x == 0 and y == 0:
        print(time)
        check = 1
        break
        
if check == 0:
    print(-1)
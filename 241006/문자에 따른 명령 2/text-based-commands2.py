s = list(input())
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

dir_num = 3

for elem in s:
    if elem == 'R':
        dir_num = (dir_num + 1) % 4
    elif elem == 'L':
        dir_num = (dir_num - 1) % 4
    elif elem == 'F':
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)
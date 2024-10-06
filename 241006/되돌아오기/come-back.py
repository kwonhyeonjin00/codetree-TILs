n = int(input())

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

direction = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}
x, y = 0, 0
time = 0
check = 0

def checking(x, y, t):
    if x == 0 and y == 0:
        print(t)
        x, y = 1001, 1001

for i in range(n):
    d, s = input().split()
    s = int(s)

    dir_num = direction[d]

    for j in range(s):
        x, y = x + dxs[dir_num], y + dys[dir_num]
        time += 1

        if x == 0 and y == 0:
            checking(x, y, time)
            check = 1
            break

if check == 0:
    print(-1)
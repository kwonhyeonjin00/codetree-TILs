n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
def in_range(x, y):
    global n
    return 1 <= x and x <= n and 1 <= y and y <= n

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

move_dir = mapper[d]


for i in range(t):
    r, c = r + dxs[move_dir], c + dys[move_dir]
    if in_range(r, c) == False:
        r, c = r - dxs[move_dir], c - dys[move_dir]
        move_dir = 3 - move_dir

print(r, c)
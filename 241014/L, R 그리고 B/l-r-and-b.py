arr = [list(input()) for _ in range(10)]

for i in range(10):
    for j in range(10):
        if arr[i][j] == 'B':
            Bx, By = i, j
        elif arr[i][j] == 'L':
            Lx, Ly = i, j

print(abs(Bx - Lx) + abs(By - Ly) - 1)
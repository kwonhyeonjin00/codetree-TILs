arr = [list(input()) for _ in range(10)]

for i in range(10):
    for j in range(10):
        if arr[i][j] == 'B':
            Bx, By = i, j
        elif arr[i][j] == 'L':
            Lx, Ly = i, j
        elif arr[i][j] == 'R':
            Rx, Ry = i, j

t = 0
if Bx == Lx == Rx and (By < Ry < Ly or By > Ry > Ly):
    t = 2
if By == Ly == Ry and (Bx < Rx < Lx or Bx > Rx > Lx):
    t = 2

print(abs(Bx - Lx) + abs(By - Ly) - 1 + t)
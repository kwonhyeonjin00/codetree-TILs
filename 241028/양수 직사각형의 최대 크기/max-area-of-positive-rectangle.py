def check2(i, column):
    row = 1

    while True:
        i += 1
        row += 1
        chk = True
        for k in column:
            if i >= n or arr[i][k] <= 0:
                chk = False

        if chk == False:
            row -= 1
            break
    return row

def check1(i, j):
    col = 1
    column = [j]
    while True:
        j += 1
        col += 1
        if j >= m or arr[i][j] <= 0:
            col -= 1
            break
        column.append(j)

    row_num = check2(i, column)
    return row_num * col

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = -1

for i in range(n):
    for j in range(m):
        t = 0
        if arr[i][j] <= 0:
            continue
        else:
            ans = max(ans, check1(i, j))

arr2 = []
for i in range(m):
    t = []
    for j in range(n):
        t.append(arr[j][i])
    arr2.append(t)

for i in range(n):
    for j in range(m):
        t = 0
        if arr2[i][j] <= 0:
            continue
        else:
            ans = max(ans, check1(i, j))

print(ans)
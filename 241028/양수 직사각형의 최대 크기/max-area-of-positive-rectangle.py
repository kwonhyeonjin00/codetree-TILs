def check2(arr3, i, column):
    row = 1

    while True:
        i += 1
        row += 1
        chk = True
        for k in column:
            if i >= dn or arr3[i][k] <= 0:
                chk = False
                break

        if chk == False:
            row -= 1
            break
    return row

def check1(arr3, i, j):
    col = 1
    column = [j]
    while True:
        j += 1
        col += 1
        if j >= dm or arr3[i][j] <= 0:
            col -= 1
            break
        else:
            column.append(j)

    row_num = check2(arr3, i, column)
    return row_num * col

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dn, dm = n, m

ans = -1

for i in range(n):
    for j in range(m):
        t = 0
        if arr[i][j] <= 0:
            continue
        else:
            ans = max(ans, check1(arr, i, j))

arr2 = []
for i in range(m):
    t = []
    for j in range(n):
        t.append(arr[j][i])
    arr2.append(t)

dn, dm = m, n

for i in range(dn):
    for j in range(dm):
        t = 0
        if arr2[i][j] <= 0:
            continue
        else:
            ans = max(ans, check1(arr2, i, j))

print(ans)
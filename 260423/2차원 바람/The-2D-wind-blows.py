n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
for r1, c1, r2, c2 in winds:
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

    temp = a[r1][c1]


    for i in range(r1, r2):
        a[i][c1] = a[i + 1][c1]
    for i in range(c1, c2):
        a[r2][i] = a[r2][i + 1]
    for i in range(r2, r1, -1):
        a[i][c2] = a[i - 1][c2]
    for i in range(c2, c1 + 1, -1):
        a[r1][i] = a[r1][i - 1]

    a[r1][c1 + 1] = temp

    b = [row[:] for row in a]

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            t = b[i][j]
            cnt = 1

            if i > 0:
                t += b[i - 1][j]
                cnt += 1
            if i < n - 1:
                t += b[i + 1][j]
                cnt += 1
            if j > 0:
                t += b[i][j - 1]
                cnt += 1
            if j < m - 1:
                t += b[i][j + 1]
                cnt += 1
            
            a[i][j] = t // cnt

for row in a:
    print(*(row))
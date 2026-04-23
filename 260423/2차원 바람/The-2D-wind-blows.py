n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
for i in range(q):
    r1, c1, r2, c2 = winds.pop(0)
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

    temp = a[r1].pop(c2)
    for i in range(1, r2 - r1):
        a[r1 + i].append(temp)
        temp = a[r1 + i].pop(c2)

    a[r2].insert(c2 + 1, temp)

    temp = a[r2].pop(c1)
    for i in range(1, r2 - r1):
        a[r2 - i].insert(c1, temp)
        temp = a[r2 - i].pop(c1 + 1)

    a[r1].insert(c1, temp)

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
            
            t //= cnt
            a[i][j] = t

for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
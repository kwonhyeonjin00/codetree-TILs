n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    x = 1
    temp = arr[i][0]
    if x == m:
        ans += 1
        continue

    for j in range(1, n):
        if temp == arr[i][j]:
            x += 1
        else:
            x = 1
            temp = arr[i][j]

        if x == m:
            ans += 1
            break

for i in range(n):
    x = 0
    temp = arr[0][i]
    if x == m:
        ans += 1
        continue

    for j in range(n):
        if temp == arr[j][i]:
            x += 1
        else:
            x = 0
            temp = arr[j][i]
        
        if x == m:
            ans += 1
            break

print(ans)
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

if m == 1:
    print(2 * n)

else:
    ans = 0

    for i in range(n):
        x = 1
        temp = arr[i][0]

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
        x = 1
        temp = arr[0][i]

        for j in range(1, n):
            if temp == arr[j][i]:
                x += 1
            else:
                x = 1
                temp = arr[j][i]
            
            if x == m:
                ans += 1
                break

    print(ans)
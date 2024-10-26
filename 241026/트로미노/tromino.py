n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n - 2):
    for j in range(m):
        temp = arr[i][j] + arr[i+1][j] + arr[i+2][j]
        ans = max(ans, temp)

for i in range(n):
    for j in range(m - 2):
        temp = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        ans = max(ans, temp)

for i in range(n - 1):
    for j in range(m - 1):
        temp = arr[i][j] + arr[i+1][j] + arr[i+1][j+1]
        ans = max(ans, temp)

        temp -= arr[i][j]
        temp += arr[i][j+1]
        ans = max(ans, temp)

        temp -= arr[i+1][j]
        temp += arr[i][j]
        ans = max(ans, temp)

        temp -= arr[i+1][j+1]
        temp += arr[i+1][j]
        ans = max(ans, temp)

print(ans)
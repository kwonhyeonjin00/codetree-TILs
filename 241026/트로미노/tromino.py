n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans1 = 0

for i in range(n - 2):
    for j in range(n):
        temp = arr[i][j] + arr[i+1][j] + arr[i+2][j]
        ans1 = max(ans1, temp)

for i in range(n):
    for j in range(n - 2):
        temp = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        ans1 = max(ans1, temp)

for i in range(n - 1):
    for j in range(n - 1):
        temp = arr[i][j] + arr[i+1][j] + arr[i+1][j+1]
        ans1 = max(ans1, temp)

        temp -= arr[i][j]
        temp += arr[i][j+1]
        ans1 = max(ans1, temp)

        temp -= arr[i+1][j]
        temp += arr[i][j]
        ans1 = max(ans1, temp)

        temp -= arr[i+1][j+1]
        temp += arr[i+1][j]
        ans1 = max(ans1, temp)

print(ans1)
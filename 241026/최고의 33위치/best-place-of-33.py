n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = -1

for i in range(1, n - 1):
    for j in range(1, n - 1):
        temp = 0
        temp += arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j-1] + arr[i][j] + arr[i][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
        ans = max(ans, temp)

print(ans)
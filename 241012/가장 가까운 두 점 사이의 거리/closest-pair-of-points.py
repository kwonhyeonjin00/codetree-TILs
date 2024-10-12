n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

ans = []

for i in range(n - 1):
    for j in range(i + 1, n):
        t = (arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2
        ans.append(t)

print(min(ans))
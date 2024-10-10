n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

for i in range(n - k + 1):
    t = 0
    for j in range(i, i + k):
        t += arr[j]

    ans = max(ans, t)

print(ans)
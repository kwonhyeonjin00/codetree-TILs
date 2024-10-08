n = int(input())

arr = list(map(int, input().split()))

ans = 0

for i in range(len(arr) - 2):
    t = 0
    for j in range(i + 2, len(arr)):
        t = arr[i] + arr[j]
        ans = max(ans, t)

print(ans)
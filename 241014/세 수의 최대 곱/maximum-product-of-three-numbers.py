n = int(input())
arr = list(map(int, input().split()))

x = -10000000000
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            t = arr[i] * arr[j] * arr[k]

            x = max(x, t)
print(x)
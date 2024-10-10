n, k = map(int, input().split())

arr = [0] * 101

for i in range(n):
    x, c = map(int, input().split())
    arr[c] += x

ans = 0

if k >= 50:
    print(sum(arr))
else:
    for i in range(100 - k*2):
        t = 0
        if i >= 0:
            for j in range(i, i + k*2 + 1):
                t += arr[j]

            ans = max(ans, t)

    print(ans)
n = int(input())

arr = [int(input()) for _ in range(n)]

ans = 10000000000

g = 0
for i in range(n):
    t = 0
    for j in range(n):
        t += arr[j] * g
        g = (g + 1) % n

    ans = min(ans, t)
    g += 1

print(ans)
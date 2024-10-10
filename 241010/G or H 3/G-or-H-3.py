max_num = 10000

arr = [0] * max_num
n, k = map(int, input().split())

for i in range(n):
    x, c = input().split()
    x = int(x)

    arr[x] = 1 if c == 'G' else 2

ans = 0

for i in range(max_num - k):
    t = 0
    for j in range(i, i + k + 1):
        t += arr[j]

    ans = max(ans, t)

print(ans)
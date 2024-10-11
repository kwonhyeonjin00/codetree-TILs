arr = list(map(int, input().split()))
def check(x, y, z):
    sum1 = arr[x] + arr[y] + arr[z]
    sum2 = sum(arr) - sum1
    return abs(sum2 - sum1)

ans = 100000000

for i in range(6):
    for j in range(6):
        for k in range(6):
            t = check(i, j, k)
        ans = min(ans, t)

print(ans)
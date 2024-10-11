n, h, t = map(int, input().split())

arr = list(map(int, input().split()))
arr2 = []
for i in range(n):
    arr2.append(abs(arr[i] - h))

ans = 10000000

for i in range(n - t + 1):
    x = 0
    for j in range(i, i + t):
        x += arr2[j]
    
    ans = min(ans, x)

print(ans)
n, h, t = map(int, input().split())

arr = list(map(int, input().split()))
arr2 = []
for i in range(n):
    arr2.append(abs(arr[i] - h))

ans = 100000

for i in range(n - t + 1):
    t = 0
    for j in range(i, i + 3):
        t += arr2[j]
    
    ans = min(ans, t)

print(ans)
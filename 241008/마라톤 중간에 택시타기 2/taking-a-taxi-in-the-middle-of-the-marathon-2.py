n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 1000000

for i in range(1, len(arr) - 1):
    tx, ty = arr[i][0], arr[i][1]
    del(arr[i])
    
    t = 0
    for j in range(len(arr) - 1):
        t += abs(arr[j][0] - arr[j + 1][0]) + abs(arr[j][1] - arr[j + 1][1])

    ans = min(ans, t)
    arr.insert(i, [tx, ty])

print(ans)
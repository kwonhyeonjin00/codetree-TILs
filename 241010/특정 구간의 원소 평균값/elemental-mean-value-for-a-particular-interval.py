n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i, n):
        t = 0
        for k in range(i, j + 1):
            t += arr[k]
        if t / (j-i+1) in arr[:k+1]:
            cnt += 1

print(cnt)
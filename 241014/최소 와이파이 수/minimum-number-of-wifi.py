n, m = map(int, input().split())
arr = list(map(int, input().split()))

t = 2 * m + 1

cnt = 0

for i in range(0, n, t):
    for j in range(t):
        if i + j < n:
            if arr[i + j] == 1:
                cnt += 1
                break

print(cnt)
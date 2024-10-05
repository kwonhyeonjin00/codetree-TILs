n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(m)]

penalty = [0 for _ in range(n+1)]

ans = -1

for i in arr:
    penalty[i] += 1

    if penalty[i] == k:
        ans = i
        break

print(ans)
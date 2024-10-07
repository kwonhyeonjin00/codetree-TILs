n = int(input())

arr = list(map(int, input().split()))

sum_min = 10000000
cur = 0
for i in range(n):
    t = 0
    for j in range(n):
        t += arr[j] * abs(j - cur)

    sum_min = min(sum_min, t)
    cur += 1


print(sum_min)
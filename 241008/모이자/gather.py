n = int(input())

arr = list(map(int, input().split()))

sum_min = 10000000
cur = 0
for i in range(n):
    t = 0
    for j in range(n):
        t += arr[j] * abs(j - i)

    sum_min = min(sum_min, t)


print(sum_min)
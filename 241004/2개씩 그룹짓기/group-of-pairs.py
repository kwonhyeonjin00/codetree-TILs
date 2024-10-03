n = int(input())
arr = list(map(int, input().split()))

arr.sort()
max = 0

for i in range(n):
    sums = arr[i] + arr[n*2-1-i]

    if sums > max:
        max = sums

print(max)
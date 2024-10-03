n = int(input())
arr = list(map(int, input().split()))

arr.sort()

sum = 0

for x in arr:
    sum += x
sum /= n

arr2 = []

for i in range(n*2-1):
    for j in range(i+1, n*2):
        if arr[i] + arr[j] >= sum:
            arr2.append(arr[i] + arr[j])

print(min(arr2))
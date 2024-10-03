n = int(input())
arr = list(map(int, input().split()))

sum = 0
for x in arr:
    sum += x/n

arr2 = []

for i in range(n*2-1):
    for j in range(i+1, n*2):
        x = arr[i] + arr[j]
        if x >= sum:
            arr2.append(x)

print(min(arr2))
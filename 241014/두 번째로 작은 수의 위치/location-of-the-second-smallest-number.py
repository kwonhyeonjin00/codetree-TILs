n = int(input())
arr = list(map(int, input().split()))

arr2 = arr

x = min(arr2)

for i in range(n):
    if arr[i] == x:
        arr[i] = 101

x = min(arr2)

if arr.count(x) == 1:
    print(arr.index(x) + 1)
else:
    print(-1)
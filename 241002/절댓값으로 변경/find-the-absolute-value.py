def z(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] *= -1
    for j in arr:
        print(j, end=' ')

n = int(input())
arr = list(map(int, input().split()))
z(arr)
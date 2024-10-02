def z(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            print(arr[i] // 2, end=' ')
        else:
            print(arr[i], end=' ')

n = int(input())
arr = list(map(int, input().split()))
z(arr)
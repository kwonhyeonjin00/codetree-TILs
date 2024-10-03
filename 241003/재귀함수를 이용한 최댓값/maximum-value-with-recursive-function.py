def maxv(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        return arr[1]
    
    if arr[0] > arr[1]:
        del(arr[1])
        return maxv(arr)
    return maxv(arr[1:])

n = int(input())
arr = list(map(int, input().split()))

print(maxv(arr))
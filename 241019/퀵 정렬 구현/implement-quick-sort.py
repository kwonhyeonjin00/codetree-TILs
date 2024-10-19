n = int(input())
arr = list(map(int, input().split()))

def merge(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def merge_sort(arr, low, high):
    if low < high:
        pos = merge(arr, low, high)

        merge_sort(arr, low, pos - 1)
        merge_sort(arr, pos + 1, high)

merge_sort(arr, 0, n - 1)
for x in arr:
    print(x, end=' ')
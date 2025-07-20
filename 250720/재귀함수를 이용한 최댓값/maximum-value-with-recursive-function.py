n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def find_max(n, arr):
    
    if n == -1:
        return 0

    return arr[n] if arr[n] > find_max(n - 1, arr) else find_max(n - 1, arr)

print(find_max(n - 1, arr))
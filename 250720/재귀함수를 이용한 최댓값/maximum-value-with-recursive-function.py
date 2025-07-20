n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def find_max(n):
    
    if n == -1:
        return 0
    x = find_max(n - 1)
    return arr[n] if arr[n] > x else x

print(find_max(n - 1))
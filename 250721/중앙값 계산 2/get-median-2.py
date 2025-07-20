n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
array = []
mid = 1

for i in range(0, n + 1, 2):
    array.append(arr[i])
    array.append(arr[i + 1])
    
    array.sort()
    print(array[mid], end=' ')
    mid += 1
n = int(input())
arr = [0 for _ in range(100)]

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a-1, b):
        arr[j] += 1

print(max(arr))
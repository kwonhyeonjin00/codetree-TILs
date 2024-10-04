n = int(input())
arr = [0 for _ in range(200)]

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a+100, b+100):
        arr[j] += 1

print(max(arr))
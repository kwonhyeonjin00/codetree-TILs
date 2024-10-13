a, b = map(int, input().split()) 
c, d = map(int, input().split())

arr = [0] * (max(b, d))

for i in range(a, b):
    arr[i] += 1
for j in range(c, d):
    arr[j] += 1

print(arr.count(1) + arr.count(2))
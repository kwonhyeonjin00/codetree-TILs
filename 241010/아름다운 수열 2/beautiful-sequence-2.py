n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

x = ""
for i in arr2:
    x += str(i)

cnt = 0

for i in range(n - m + 1):
    t = 0
    for j in range(i, i + m):
        if str(arr1[j]) in x:
            t += 1
        if t == m:
            cnt += 1

print(cnt)
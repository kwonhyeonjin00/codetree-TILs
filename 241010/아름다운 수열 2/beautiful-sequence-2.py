n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr2.sort()

cnt = 0

for i in range(n - m + 1):
    t = arr1[i:i+m]
    t.sort()
    if t == arr2:
        cnt += 1


print(cnt)
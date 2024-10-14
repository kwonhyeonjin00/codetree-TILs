n = int(input())
arr = list(map(int, input().split()))

arr0 = []
arr1 = []

for i in arr:
    if i >= 0:
        arr0.append(i)
    else:
        arr1.append(i)

if arr0:
    t1 = max(arr0)
    arr0.pop(arr0.index(t1))
else:
    t1 = -1001

if arr0:
    t2 = max(arr0)
    arr0.pop(arr0.index(t2))
else:
    t2 = -1001

if arr0:
    t3 = max(arr0)
    arr0.pop(arr0.index(t3))
else:
    t3 = -1001

if arr1:
    t4 = min(arr1)
    arr1.pop(arr1.index(t4))
else:
    t4 = -1001

if arr1:
    t5 = min(arr1)
    arr1.pop(arr1.index(t5))
else:
    t5 = -1001

if t1 == -1001:
    t6 = min(arr1)
    arr1.pop(arr1.index(t6))
else:
    t6 = t1
print(max(t1 * t2 * t3, t4 * t5 * t6))
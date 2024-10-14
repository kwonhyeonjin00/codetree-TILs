n = int(input())
arr = list(map(int, input().split()))

t1 = max(arr)
arr.pop(arr.index(t1))

t2 = max(arr)
arr.pop(arr.index(t2))

t3 = max(arr)
arr.pop(arr.index(t3))

if arr:
    t4 = min(arr)
    arr.pop(arr.index(t4))
    if arr:
        t5 = min(arr)
        arr.pop(arr.index(t5))
        print(max(t1 * t2 * t3, t1 * t4 * t5))
    else:
        print(t1 * t2 * t3) 
else:
    print(t1 * t2 * t3)
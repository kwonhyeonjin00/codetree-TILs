n, s = map(int, input().split())

arr = list(map(int, input().split()))

min_num = 10000000

for i in range(n - 1):
    for j in range(i + 1, n):
        t1 = arr.pop(j)
        t2 = arr.pop(i)
        h = sum(arr)
        min_num = min(min_num, abs(s - h))
        arr.insert(i, t2)
        arr.insert(j, t1)



print(min_num)
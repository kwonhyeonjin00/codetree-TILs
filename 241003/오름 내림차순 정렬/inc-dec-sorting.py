def f(arr):
    for i in arr:
        print(i, end=' ')
    print()

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
f(arr)
arr.sort(reverse=True)
f(arr)
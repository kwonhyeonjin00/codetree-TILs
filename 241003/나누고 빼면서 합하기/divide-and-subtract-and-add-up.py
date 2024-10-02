def z(arr, m):
    x = 0
    while m != 0:
        x += arr[m-1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    print(x)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
z(arr, m)
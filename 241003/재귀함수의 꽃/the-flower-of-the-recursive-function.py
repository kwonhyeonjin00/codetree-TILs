def z(n):
    if n == 0:
        return
    print(n, end=' ')
    z(n-1)
    print(n, end=' ')


n = int(input())
z(n)
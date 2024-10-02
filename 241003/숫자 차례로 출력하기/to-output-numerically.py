def big(n):
    if n == 0:
        return

    big(n-1)
    print(n, end=' ')

def small(n):
    if n == 0:
        return
    print(n, end=' ')
    small(n-1)

n = int(input())
big(n)
print()
small(n)
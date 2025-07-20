N = int(input())

# Please write your code here.
def rec(n):
    if n == 0:
        return

    print(n, end=' ')
    rec(n - 1)
    print(n, end=' ')

rec(N)
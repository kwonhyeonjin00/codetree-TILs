N = int(input())

# Please write your code here.
def rec(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return rec(n / 2) + 1

    else:
        return rec(n // 3) + 1

print(rec(N))
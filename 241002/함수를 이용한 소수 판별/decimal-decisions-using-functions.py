def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

x = 0
n, m = map(int, input().split())

for i in range(n, m+1):
    if is_prime(i):
        x += i

print(x)
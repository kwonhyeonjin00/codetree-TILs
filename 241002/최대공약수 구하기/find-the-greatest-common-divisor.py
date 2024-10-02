def max(n, m):
    if n < m:
        n, m = m, n
    for i in range(n, 0, -1):
        if n % i == 0 and m % i == 0:
            print(i)
            break 

n, m = map(int, input().split())
max(n, m)
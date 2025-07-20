n, m = map(int, input().split())

# Please write your code here.
def lcm(n, m):
    x = 1
    for i in range(2, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            x = i
    print(int(n / x * m))

lcm(n, m)
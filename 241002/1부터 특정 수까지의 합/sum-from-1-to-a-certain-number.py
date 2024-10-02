def hap(n):
    a = 0
    for i in range(n+1):
        a += i
    a //= 10
    return a

n = int(input())

print(hap(n))
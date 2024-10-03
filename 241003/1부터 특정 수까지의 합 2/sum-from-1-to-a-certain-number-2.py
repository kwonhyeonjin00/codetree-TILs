def hap(n):
    if n == 0:
        return 0
    return n + hap(n-1)

n = int(input())
print(hap(n))
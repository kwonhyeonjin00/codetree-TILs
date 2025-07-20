N = int(input())

# Please write your code here.
def hap(n):
    if n < 10:
        return n ** 2

    return hap(n // 10) + (n % 10) ** 2

print(hap(N))
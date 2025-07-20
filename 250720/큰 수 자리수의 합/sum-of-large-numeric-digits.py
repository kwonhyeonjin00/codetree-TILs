a, b, c = map(int, input().split())

# Please write your code here.
def hap(n):
    if n == 0:
        return 0

    return hap(n // 10) + n % 10

print(hap(a*b*c))
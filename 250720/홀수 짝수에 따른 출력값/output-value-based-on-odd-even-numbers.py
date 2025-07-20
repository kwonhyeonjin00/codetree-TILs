

# Please write your code here.
def hap(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    return hap(n - 2) + n
N = int(input())
print(hap(N))

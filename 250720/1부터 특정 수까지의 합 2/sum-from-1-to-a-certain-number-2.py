N = int(input())

# Please write your code here.
def hap(n):
    if n == 1:
        return 1

    return hap(n - 1) + n

print(hap(N))
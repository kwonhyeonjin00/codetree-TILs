N = int(input())

# Please write your code here.
def cal(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    return cal(n - 1) + cal(n // 3)

print(cal(N))
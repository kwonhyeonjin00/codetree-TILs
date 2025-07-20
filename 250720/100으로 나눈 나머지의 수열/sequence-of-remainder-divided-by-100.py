N = int(input())

# Please write your code here.
def cal(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4

    return cal(n - 1) * cal(n - 2) % 100

print(cal(N))
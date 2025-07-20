n = int(input())

# Please write your code here.
def re(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

x = re(n)
x //= 10

print(x)
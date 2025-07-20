n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def lcm(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return a * b // i

def cal(n):
    if n == 0:
        return arr[0] 

    return lcm(cal(n - 1), arr[n])

print(cal(n - 1))
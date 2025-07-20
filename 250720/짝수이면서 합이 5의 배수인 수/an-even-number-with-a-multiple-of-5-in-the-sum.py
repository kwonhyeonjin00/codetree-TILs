n = int(input())

# Please write your code here.
def cal(n):
    if n % 2 == 0 and (n // 10 + n % 10) % 5 == 0:
        return "Yes"
    return "No"

print(cal(n))
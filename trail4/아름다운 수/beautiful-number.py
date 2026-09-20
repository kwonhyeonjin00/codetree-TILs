n = int(input())

# Please write your code here.

def cal(n):
    if n == 4:
        return 8
    if n == 3:
        return 4
    if n == 2:
        return 2
    if n == 1:
        return 1
    if n == 0:
        return 0
    
    if n >= 5:
        return cal(n - 1) + cal(n - 2) + cal(n - 3) + cal(n - 4)
    
print(cal(n))
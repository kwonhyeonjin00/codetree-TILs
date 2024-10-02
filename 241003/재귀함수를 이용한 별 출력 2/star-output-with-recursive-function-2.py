def function1(n):
    if n < 1:
        return
    print('* ' * n)
    function1(n-1)

def function2(num):
    if num > n:
        return
    print('* ' * num)
    function2(num+1)

n = int(input())
function1(n)
function2(1)
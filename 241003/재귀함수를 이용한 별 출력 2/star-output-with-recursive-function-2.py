def function1(n):
    for i in range(n):
        for j in range(5-i):
            print('*', end=' ')
        print()

def function2(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        print()

n = int(input())
function1(n)
function2(n)
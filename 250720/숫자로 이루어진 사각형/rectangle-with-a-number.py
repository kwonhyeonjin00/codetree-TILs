n = int(input())

# Please write your code here.
def p(n):
    x = 1
    for i in range(n):
        for j in range(n):
            print(x, end=' ')
            if x == 9:
                x -= 8
            else:
                x += 1
        print()

p(n)
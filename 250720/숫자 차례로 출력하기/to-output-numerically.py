n = int(input())

# Please write your code here.
def rev(n):
    if n == 0:
        return
    
    print(n, end=' ')
    rev(n - 1)

def order(n):
    if n == 0:
        return
    
    order(n - 1)
    print(n, end= ' ')

order(n)
print()
rev(n)
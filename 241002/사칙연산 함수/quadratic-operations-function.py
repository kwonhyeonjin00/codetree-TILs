def sik(a, b, c):
    if b == "+":
        print(a + c)    
    elif b == "-":
        print(a - c)
    elif b == "*":
        print(a * c)
    elif b == "/":
        print(a / c)

a, b, c = input().split()

a, c = int(a), int(c)

print(f'{a} {b} {c} = ', end='')
sik(a, b, c)
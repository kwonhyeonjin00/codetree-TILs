def sik(a, b, c):
    if b == "+":
        print(f'{a} {b} {c} = {a + c}')    
    elif b == "-":
        print(f'{a} {b} {c} = {a - c}')
    elif b == "*":
        print(f'{a} {b} {c} = {a * c}')
    elif b == "/":
        print(f'{a} {b} {c} = {a // c}')
    else:
        print("False")

a, b, c = input().split()

a, c = int(a), int(c)

print(f'{a} {b} {c} = {a + c}')
sik(a, b, c)
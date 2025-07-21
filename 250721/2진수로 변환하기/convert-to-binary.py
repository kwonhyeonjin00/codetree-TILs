n = int(input())

# Please write your code here.
digits = []

while True:
    if n == 1 or n == 0:
        digits.append(n)
        break

    digits.append(n % 2)
    n //= 2

for x in digits[::-1]:
    print(x, end='')
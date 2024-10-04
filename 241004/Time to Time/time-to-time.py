a, b, c, d = map(int, input().split())

z = 0

while True:
    if a == c and b == d:
        break

    b += 1
    z += 1
    if b == 60:
        a += 1
        b -= 60

print(z)
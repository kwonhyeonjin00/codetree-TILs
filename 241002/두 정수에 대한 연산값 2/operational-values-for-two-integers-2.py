def z(a, b):
    if a < b:
        a += 10
        b *= 2
    else:
        b += 10
        a *= 2
    return a, b

a, b = map(int, input().split())

a, b = z(a, b)
print(a, b)
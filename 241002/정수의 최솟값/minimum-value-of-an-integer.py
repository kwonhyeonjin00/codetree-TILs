def min(a, b, c):
    if a <= b and a <= c:
        print(a)
    elif b <= a and b <= c:
        print(b)
    elif c <= a and c <= b:
        print(c)
a, b, c = map(int, input().split())

min(a, b, c)
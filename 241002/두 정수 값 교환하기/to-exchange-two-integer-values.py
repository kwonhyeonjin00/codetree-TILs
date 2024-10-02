def swap(a, b):
    return b, a

n, m = map(int, input().split())
a, b = swap(n, m)
print(a, b)
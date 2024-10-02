def swap(a, b):
    arr = [b, a]
    return arr

n, m = map(int, input().split())
for x in swap(n, m):
    print(x, end=' ')
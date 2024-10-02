def z(a1, a2):
    x = 0
    global arr
    for i in range(a1-1, a2):
        x += arr[i]
    return x

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(m):
    a1, a2 = map(int, input().split())
    x = z(a1, a2)
    print(x)
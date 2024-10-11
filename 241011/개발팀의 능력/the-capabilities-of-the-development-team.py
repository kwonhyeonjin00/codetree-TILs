def check_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    if c > a and c > b:
        return c

def check_min(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    if c <= a and c <= b:
        return c

arr = list(map(int, input().split()))
arr.sort()
t1 = arr[4]
x = 0
y = 0
if arr[0] + arr[3] == t1 or arr[2] + arr[3] == t1 or arr[0] + arr[3] == arr[2] + arr[3]:
    z1 = 100000
else:
    x = check_max(arr[0] + arr[3], arr[2] + arr[3], t1)
    y = check_min(arr[0] + arr[3], arr[2] + arr[3], t1)
    z1 = x - y

if arr[0] + arr[2] == t1 or arr[1] + arr[3] == t1 or arr[0] + arr[2] == arr[1] + arr[3]:
    z2 = 100000
else:
    x = check_max(arr[0] + arr[2], arr[1] + arr[3], t1)
    y = check_min(arr[0] + arr[2], arr[1] + arr[3], t1)
    z2 = x - y
if arr[0] + arr[1] == t1 or arr[2] + arr[3] == t1 or arr[0] + arr[1] == arr[2] + arr[3]:
    z3 = 100000
else:
    x = check_max(arr[0] + arr[1], arr[2] + arr[3], t1)
    y = check_min(arr[0] + arr[1], arr[2] + arr[3], t1)
    z3 = x - y

if x == 0 and y == 0:
    print(-1)
else:
    print(check_min(z1, z2, z3))
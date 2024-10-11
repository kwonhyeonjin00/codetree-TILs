arr = list(map(int, input().split()))
arr.sort()
a = arr[0] + arr[5]
b = arr[1] + arr[4]
c = arr[2] + arr[3]

if a >= b and a >= c:
    max_s = a
elif b >= a and b >= c:
    max_s = b
elif c >= a and c >= b:
    max_s = c

if a <= b and a <= c:
    min_s = a
elif b <= a and b <= c:
    min_s = b
elif c <= a and c <= b:
    min_s = c

print(max_s - min_s)
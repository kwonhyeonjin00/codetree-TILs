arr = list(map(int, input().split()))
arr.sort()
a, b, c = arr[0], arr[1], arr[2]

if a + 1 == b and b + 1 == c:
    print(0)
elif a + 1 == b or b + 1 == c:
    print(2)
elif a + 2 == b or b + 2 == c:
    print(1)
else:
    print(2)
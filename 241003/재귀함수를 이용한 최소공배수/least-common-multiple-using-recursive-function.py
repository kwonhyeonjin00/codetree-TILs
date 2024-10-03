def g(a, b):
    if a > b:
        a, b = b, a
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def f(arr):
    # 종료 조건
    if len(arr) == 1:
        return arr[0]

    # 점화식
    a, b = arr[0], arr[1]
    arr[0] = int(a / g(a, b) * b)
    del(arr[1])
    return f(arr)

n = int(input())
arr = list(map(int, input().split()))
print(f(arr))
def f(n):
    # 종료 조건
    if n == 0 or n == 1:
        return 1

    # 점화식
    return f(n - 1) * n

n = int(input())
print(f(n))
cnt = 0

def f(n):
    global cnt
    if n == 1:
        return cnt
    cnt += 1

    if n % 2 == 0:
        return f(n/2)
    return f(n*3+1)

n = int(input())
print(f(n))
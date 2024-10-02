def sosu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def even(n):
    if (n//10 + n%10) % 2 == 0:
        return True
    return False

a, b = map(int, input().split())
cnt = 0
arr = []
for i in range(a, b+1):
    if sosu(i):
        arr.append(i)

for i in arr:
    if even(i):
        cnt += 1

print(cnt)
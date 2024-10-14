n = int(input())
arr = []

s = 0
for i in range(n):
    x = int(input())
    s += x
    arr.append(x)

mean = int(s / n)

ans = 0

for i in arr:
    if i > mean:
        ans += (i - mean)

print(ans)
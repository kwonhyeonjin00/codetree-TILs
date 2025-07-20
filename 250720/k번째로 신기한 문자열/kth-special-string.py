n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
arr = []
for i in range(n - 1):
    c = 1
    for j in range(len(t)):
        if str[i][j] != t[j]:
            c = 0
            break
    if c == 1:
        arr.append(str[i])

print(sorted(arr)[k - 1])
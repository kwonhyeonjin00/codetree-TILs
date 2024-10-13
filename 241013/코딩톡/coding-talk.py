n, m, p = map(int, input().split())
arr = []
chk = []

for i in range(65, 65 + n):
    arr.append(chr(i))

ans = [[] for _ in range(m)]


for j in range(m):
    c, u = input().split()

    for k in range(j+1):
        ans[k].append(c)
    chk.append(int(u))


for l in range(n):
    if chk[p-1] != 0:
        if arr[l] in ans[p-1]:
            pass
        else:
            print(arr[l], end=' ')
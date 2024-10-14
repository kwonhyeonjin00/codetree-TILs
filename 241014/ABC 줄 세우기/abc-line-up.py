n = int(input())
arr = list(map(str, input().split()))

cnt = 0

for i in range(65, 65 + n):
    for j in range(n):
        if arr[j] == chr(i):
            cnt += j
            arr.pop(j)
            break

print(cnt)
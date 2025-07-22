n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt = 0
ans = 1

for i in range(0, n):

    if i >= 1 and arr[i] * arr[i - 1] > 0:
        cnt += 1

    else:
        cnt = 1

    ans = max(ans, cnt)

print(ans)
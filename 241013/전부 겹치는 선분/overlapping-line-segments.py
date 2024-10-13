n = int(input())

arr_x1 = []
arr_x2 = []

for i in range(n):
    a, b = map(int, input().split())
    arr_x1.append(a)
    arr_x2.append(b)

ans = [0] * (max(arr_x2) + 1)

for i in range(n):
    for j in range(arr_x1[i], arr_x2[i] + 1):
        ans[j] += 1
    #print(ans)
if n in ans:
    print("Yes")
else:
    print("No")
def check(a1, a2, a3):
    if a1[0] == a2[0] and a1[1] == a3[1]:
        return abs(a1[1] - a2[1]) * abs(a1[0] - a3[0])
    elif a1[0] == a3[0] and a1[1] == a2[1]:
        return abs(a1[1] - a3[1]) * abs(a1[0] - a2[0])

    elif a2[0] == a1[0] and a2[1] == a3[1]:
        return abs(a2[1] - a1[1]) * abs(a2[0] - a3[0])
    elif a2[1] == a1[1] and a2[0] == a3[0]:
        return abs(a2[0] - a1[0]) * abs(a2[1] - a3[1])

    elif a3[0] == a1[0] and a3[1] == a2[1]:
        return abs(a3[1] - a1[1]) * abs(a3[0] - a2[0])
    elif a3[1] == a1[1] and a3[0] == a2[0]:
        return abs(a3[0] - a1[0]) * abs(a3[1] - a2[1])
    return 0

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            t = check(arr[i], arr[j], arr[k])

            ans = max(ans, t)

print(ans)
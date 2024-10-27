def move_m2(i, j, m1, m2):
    num = 0
    for k in range(m2):
        i -= 1
        j -= 1
        num += arr[i][j]
    
    for l in range(m1):
        i += 1
        j -= 1
        num += arr[i][j]

    for o in range(m2-1):
        i += 1
        j += 1
        num += arr[i][j]
    return num

def move_m1(i, j, m1):
    arr_t = []

    num = arr[i][j]
    for k in range(m1):
        i -= 1
        j += 1
        num += arr[i][j]
    m2 = min(j - m1, i)
    for l in range(1, m2+1):
        t = num
        t += move_m2(i, j, m1, l)
        arr_t.append(t)
    return arr_t

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(2, n):
    for j in range(1, n - 1):
        m1 = min(n-1-j, i-1)
        for k in range(1, m1+1):
            temp = move_m1(i, j, k)
            ans = max(ans, max(temp))

print(ans)
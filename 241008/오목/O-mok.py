arr = [list(map(int, input().split())) for _ in range(19)]
def check(n):
    for i in range(19):
        for j in range(15):
            if arr[i][j] == n and arr[i][j + 1] == n and arr[i][j + 2] == n and arr[i][j + 3] == n and arr[i][j + 4] == n:
                return i + 1, j + 3
    for i in range(15):
        for j in range(19):
            if arr[i][j] == n and arr[i + 1][j] == n and arr[i + 2][j] == n and arr[i + 3][j] == n and arr[i + 4][j] == n:
                return i + 3, j + 1
    for i in range(15):
        for j in range(15):
            if arr[i][j] == n and arr[i + 1][j + 1] == n and arr[i + 2][j + 2] == n and arr[i + 3][j + 3] == n and arr[i + 4][j + 4] == n:
                return i + 3, j + 3
    for i in range(15):
        for j in range(4, 19):
            if arr[i][j] == n and arr[i + 1][j - 1] == n and arr[i + 2][j - 2] == n and arr[i + 3][j - 3] == n and arr[i + 4][j - 4] == n:
                return i + 3, j - 1
    return -1, -1


x, y = check(1)
if x != -1:
    print("1")
    print(x, y)
else:
    x, y = check(2)
    if x != -1:
        print("2")
        print(x, y)
    else:
        print(0)
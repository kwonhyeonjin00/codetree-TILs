n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m - 2):
        if arr[i][j] == 'L' and arr[i][j + 1] == 'E' and arr[i][j + 2] == 'E':
            cnt += 1

for i in range(n):
    for j in range(2, m):
        if arr[i][j] == 'L' and arr[i][j - 1] == 'E' and arr[i][j - 2] == 'E':
            cnt += 1

for i in range(n - 2):
    for j in range(m):
        if arr[i][j] == 'L' and arr[i + 1][j] == 'E' and arr[i + 2][j] == 'E':
            cnt += 1

for i in range(2, n):
    for j in range(m):
        if arr[i][j] == 'L' and arr[i - 1][j] == 'E' and arr[i - 2][j] == 'E':
            cnt += 1
        
for i in range(n - 2):
    for j in range(m - 2):
        if arr[i][j] == 'L' and arr[i + 1][j + 1] == 'E' and arr[i + 2][j + 2] == 'E':
            cnt += 1

for i in range(n - 2):
    for j in range(2, m):
        if arr[i][j] == 'L' and arr[i + 1][j - 1] == 'E' and arr[i + 2][j - 2] == 'E':
            cnt += 1

for i in range(2, n):
    for j in range(m - 2):
        if arr[i][j] == 'L' and arr[i - 1][j + 1] == 'E' and arr[i - 2][j + 2] == 'E':
            cnt += 1

for i in range(2, n):
    for j in range(2, m):
        if arr[i][j] == 'L' and arr[i - 1][j - 1] == 'E' and arr[i - 2][j - 2] == 'E':
            cnt += 1

print(cnt)
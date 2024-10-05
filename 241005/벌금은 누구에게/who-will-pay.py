def check(arr):
    global checking
    for i in range(len(arr)):
        if arr[i] == k:
            checking = 1
            return i+1
    return 0

n, m, k = map(int, input().split())
arr = [0 for _ in range(n)]
checking = 0

while True:
    if checking == 1 or m == 0:
        break 
    x = int(input())
    arr[x-1] += 1
    t = check(arr)
    if t != 0:
        print(t)
    m -= 1

if checking == 0:
    print(-1)
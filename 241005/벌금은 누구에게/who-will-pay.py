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

while checking == 0:
    x = int(input())
    arr[x-1] += 1
    t = check(arr)
    if t != 0:
        print(t)

if checking == 0:
    print(-1)
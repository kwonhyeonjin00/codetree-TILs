n, m = map(int, input().split())
arr = list(map(int, input().split()))

t = 2 * m + 1

cnt = 0

while True:
    if arr:
        if arr[0] == 0:
            arr.pop(0)
        elif arr[0] == 1:
            arr.pop(0)
            arr.pop(0)
            arr.pop(0)
            cnt += 1
    else:
        break

print(cnt)
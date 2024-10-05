n, k, p, T = map(int, input().split())
hand = []

for i in range(T):
    t, x, y = map(int, input().split())
    hand.append([t, x, y])
hand.sort(key=lambda x: x)

arr = [0] * (n + 1)
dis = [0] * (n + 1)


arr[p] = 1
dis[p] = k
cnt = 0

for t, x, y in hand:
    if dis[x] > 0 and arr[y] == 0:
        dis[y] = k
        arr[y] = 1
        dis[x] -= 1
        cnt += 1
    elif dis[y] > 0 and arr[x] == 0:
        dis[x] = k
        arr[x] = 1
        dis[y] -= 1
        cnt += 1
    elif dis[y] > 0 and dis[x] > 0:
        dis[x] -= 1
        dis[y] -= 1
        cnt += 1
    
arr.pop(0)
for i in arr:
    print(i, end='')
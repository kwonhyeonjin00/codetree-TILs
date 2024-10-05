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

for t, x, y in hand:
    if dis[y] > 0 and dis[x] > 0:
        dis[x] -= 1
        dis[y] -= 1

    elif dis[x] > 0 and dis[y] == 0:
        if arr[y] == 0:
            dis[y] = k
            arr[y] = 1
        dis[x] -= 1

    elif dis[y] > 0 and dis[x] == 0:
        if arr[x] == 0:
            dis[x] = k
            arr[x] = 1
        dis[y] -= 1

arr.pop(0)
for i in arr:
    print(i, end='')
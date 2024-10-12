n = int(input())

arr_x = []
arr_y = []

ans = []

for i in range(n):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

for i in range(n):
    
    for j in range(n):
        if j == i:
            tx = arr_x.pop(i)
            ty = arr_y.pop(i)

        max_x = max(arr_x)
        max_y = max(arr_y)
        min_x = min(arr_x)
        min_y = min(arr_y)

        ans.append((max_x - min_x) * (max_y - min_y))

    arr_x.insert(i, tx)
    arr_y.insert(i, ty)

print(min(ans))
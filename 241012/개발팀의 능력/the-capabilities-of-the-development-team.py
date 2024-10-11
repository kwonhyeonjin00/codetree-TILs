def check_max(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    
def check_min(x, y, z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    elif z < x and z < y:
        return z 

arr = list(map(int, input().split()))
arr3 = []
for i in range(5):
    t1 = arr[i]
    temp = arr.pop(i)

    for j in range(3):
        t2 = arr[3] + arr[j]
        t3 = sum(arr) - t2

        if t1 != t2 and t2 != t3 and t1 != t3:
            max_num = check_max(t1, t2, t3)
            min_num = check_min(t1, t2, t3)
            arr3.append(max_num - min_num)

    arr.insert(i, temp)
if arr3:
    print(min(arr3))
else:
    print(-1)
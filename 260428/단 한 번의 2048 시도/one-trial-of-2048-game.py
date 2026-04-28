# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Please write your code here.
# 왼쪽 기준
def push_list(arr):
    arr = [x for x in arr if x > 0]
    while len(arr) < 4:
        arr.append(0)

    lst = [0] * 4

    if arr[0] == arr[1]:
        lst[0] = arr[0] + arr[1]

        if arr[2] == arr[3]:
            lst[1] = arr[2] + arr[3]

        else:
            lst[1] = arr[2]
            lst[2] = arr[3]

    else:
        lst[0] = arr[0]
        lst[1] = arr[1]

        if arr[1] == arr[2]:
            lst[1] += arr[2]
            lst[2] = arr[3]

        else:
            if arr[2] == arr[3]:
                lst[2] = arr[2] + arr[3]
            else:
                lst[2] = arr[2]
                lst[3] = arr[3]
    return lst

ans = []

if dir == 'L':
    for row in grid:
        ans.append(push_list(row))
    for row in ans:
        print(*row)

elif dir == 'R':
    for row in grid:
        ans.append(push_list(row[::-1]))      
    for row in ans:
        print(*row[::-1])

elif dir == 'U':
    grid = list(map(list, zip(*grid)))
    for row in grid:
        ans.append(push_list(row))
    ans = list(map(list, zip(*ans)))
    for row in ans:
        print(*row)

elif dir == 'D':
    grid = list(map(list, zip(*grid)))
    for row in grid:
        ans.append(push_list(row[::-1]))
    ans = list(map(list, zip(*ans)))
    ans = ans[::-1]   
    
    for row in ans:
        print(*row)
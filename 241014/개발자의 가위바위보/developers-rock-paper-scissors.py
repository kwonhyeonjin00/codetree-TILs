def fir(arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i][0] == 1 and arr[i][1] == 2:
            cnt += 1
        elif arr[i][0] == 2 and arr[i][1] == 3:
            cnt += 1
        elif arr[i][0] == 3 and arr[i][1] == 1:
            cnt += 1  
    return cnt 
def sec(arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i][0] == 1 and arr[i][1] == 3:
            cnt += 1
        elif arr[i][0] == 2 and arr[i][1] == 1:
            cnt += 1
        elif arr[i][0] == 3 and arr[i][1] == 2:
            cnt += 1
    return cnt

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
ans = []

ans.append(fir(arr))
ans.append(sec(arr))

print(max(ans))
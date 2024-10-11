n = int(input())

arr = [0] * 101
for i in range(n):
    x, c = input().split()
    x = int(x)
    arr[x] = 1 if c == 'G' else 2

ans = 0

for i in range(101):
    for j in range(i + 1, 101):
        if arr[i] == 0 or arr[j] == 0:
            continue
        
        cnt_h = 0
        cnt_g = 0

        for k in range(i, j+1):
            if arr[k] == 1:
                cnt_g += 1
            elif arr[k] == 2:
                cnt_h += 1
        
        if cnt_g == cnt_h or cnt_g == 0 or cnt_h == 0:
            ans = max(ans, j-i)
print(ans)
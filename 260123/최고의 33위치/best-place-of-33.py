n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
maxx = 0

for i in range(n - 2):
    
    for j in range(n - 2):  
        cnt = 0    
        cnt += grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2] + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2] 

    maxx = max(maxx, cnt)

print(maxx)
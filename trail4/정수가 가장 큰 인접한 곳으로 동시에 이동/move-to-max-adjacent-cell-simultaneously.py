n, m, t = map(int, input().split())

# Create n x n grid
grid = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
# 상하좌우
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

arr = [[0 for _ in range(n)] for _ in range(n)]
count = [[0 for _ in range(n)] for _ in range(n)]

# 구슬 인접 칸의 인덱스 범위 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n 

# 현재 칸, 인접 칸 비교
def move(x, y):
    max_val = 0
    temp_x, temp_y = x, y
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if in_range(nx, ny):
            if grid[nx][ny] > max_val:
                max_val = grid[nx][ny]
                temp_x, temp_y = nx, ny
                
    return temp_x, temp_y

# arr에 구슬 위치 적기
for pos in marbles:
    dx, dy = pos
    arr[dx - 1][dy - 1] = 1

# 구슬 위치를 move 함수로 보냄
for i in range(t):
    count = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if arr[j][k] == 1:
                arr[j][k] = 0
                next_x, next_y = move(j, k)
                count[next_x][next_y] += 1

    # 겹치는 구슬 제거
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0

    # count를 현재(arr)로 옮김
    arr = count

total = sum(row.count(1) for row in arr)
print(total) 
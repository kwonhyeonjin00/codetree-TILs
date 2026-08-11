n, m, r, c = map(int, input().split())

# Please write your code here.

board = [[0 for _ in range(n)] for _ in range(n)]
r, c = r - 1, c - 1

board[r][c] = 1

# 폭탄이 새로 생길 위치를 리턴하는 함수
def bomb(arr, m):
    cr_bomb = []
    for row in arr:
        ro, co = row
        if ro - m >= 0:
            cr_bomb.append([ro - m, co])
        if ro + m < n:
            cr_bomb.append([ro + m, co])
        if co - m >= 0:
            cr_bomb.append([ro, co - m])
        if co + m < n:
            cr_bomb.append([ro, co + m])
    return cr_bomb

for i in range(m):
    # 폭탄 위치 리스트와 시간을 함수로 보냄.
    arr = []
    for j in range(n):
        for k in range(n):
            if board[j][k] == 1:
                arr.append([j, k])

    pos_list = bomb(arr, 2**i)
    # 폭탄이 새로 생길 위치를 1로 변경
    for row in pos_list:
        ro, co = row
        board[ro][co] = 1

cnt = 0
for row in board:
    cnt += sum(row)

print(cnt)
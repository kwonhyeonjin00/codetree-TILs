from itertools import permutations

nums = [1,2,3,4,5,6,7,8,9]
perm = list(permutations(nums, 3))

n = int(input())

# 숫자 스트라이크 볼 입력받기
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for elem in perm:
    elem = list(elem)
    i, j, k = elem[0], elem[1], elem[2]

    zz = True

    for a, s, b in arr:
        
        cnt_s = 0
        cnt_b = 0

        x, y, z = a // 100, (a // 10) % 10, a % 10 #입력받은 숫자

        if x == i:
            cnt_s += 1
        if y == j:
            cnt_s += 1
        if z == k:
            cnt_s += 1
        if x == j or x == k:
            cnt_b += 1
        if y == i or y == k:
            cnt_b += 1
        if z == i or z == j:
            cnt_b += 1
        
        if cnt_s != s or cnt_b != b:
            zz = False
            break
        
    if zz:
        cnt += 1

print(cnt)
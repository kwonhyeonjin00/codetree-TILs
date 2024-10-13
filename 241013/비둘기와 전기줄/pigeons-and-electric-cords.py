n = int(input())

arr_s = [0]
arr_t = [0]

cnt = 0

for i in range(n):
    s, t = map(int, input().split())
    if s in arr_s:
        if t != arr_t[arr_s.index(s)]:
            arr_t[arr_s.index(s)] = t
            cnt += 1
    else:
        arr_s.append(s)
        arr_t.append(t)

print(cnt)
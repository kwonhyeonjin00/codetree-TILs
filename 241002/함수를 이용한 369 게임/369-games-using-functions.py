def is_magic_number(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i % 3 == 0:
            cnt += 1
        elif "3" in str(i) or "6" in str(i) or "9" in str(i):
            cnt += 1
    return cnt

a, b = map(int, input().split())
cnt = 0


cnt = is_magic_number(a, b)
print(cnt)
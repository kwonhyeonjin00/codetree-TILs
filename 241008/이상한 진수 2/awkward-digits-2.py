def two(n):
    num = 0
    t = len(n) - 1
    for i in range(t+1):
        num += 2 ** t * int(n[i]) 
        t -= 1
    return num

s = list(input())

ans = 0

for i in range(len(s)):
    if s[i] == '0':
        s[i] = '1'
        t = two(s)
        ans = max(ans, t)
        s[i] = '0'
    elif s[i] == '1':
        s[i] = '0'
        t = two(s)
        ans = max(ans, t)
        s[i] = '1'

print(ans)
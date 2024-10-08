s = list(input())

for i in range(len(s)):
    if s[i] == '0':
        s[i] = '1'
        break

n = 0
t = len(s) - 1

for i in s:
    n += 2 ** t * int(i)
    t -= 1

print(n)
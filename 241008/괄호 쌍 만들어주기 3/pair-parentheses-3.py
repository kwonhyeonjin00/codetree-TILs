s = list(input())

cnt = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == '(' and s[j] == ')':
            cnt += 1

print(cnt)
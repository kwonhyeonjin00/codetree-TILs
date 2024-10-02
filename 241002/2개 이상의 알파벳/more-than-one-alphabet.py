def check(s):
    if len(s) == 1:
        return False
    else:
        for i in range(len(s)):
            if s[i] != s[i+1]:
                return True
    return False

s = input()
if check(s):
    print("Yes")
else:
    pritn("No")
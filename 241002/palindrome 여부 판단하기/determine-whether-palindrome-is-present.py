def palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

s = input()
if palindrome(s):
    print("Yes")
else:
    print("No")
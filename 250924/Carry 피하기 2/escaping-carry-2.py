n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
carry = -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            chk = 0
            a = str(arr[i])
            b = str(arr[j])
            c = str(arr[k])
            l = max(len(a), len(b), len(c))
            a = '0' * (l - len(a)) + a
            b = '0' * (l - len(b)) + b
            c = '0' * (l - len(c)) + c

            for m in range(l):
                if int(a[m]) + int(b[m]) + int(c[m]) >= 10:
                    chk = 1
                    break
            if chk == 0:
                carry = max(carry , int(a) + int(b) + int(c))

print(carry)
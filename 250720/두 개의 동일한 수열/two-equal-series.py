n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()
c = 1

for i in range(len(A)):
    if A[i] == B[i]:
        continue
    else:
        print("No")
        c = 0
        break

if c == 1:
    print("Yes")
A = input()

# Please write your code here.
A = list(A)

for i in range(len(A)):
    if A[0] == A[-1]:
        A.insert(0, A.pop())
    else:
        break

def chk(A):
    A.append(0)
    temp = A[0]
    cnt = 0
    length = ""
    for x in A:
        if temp == x:
            cnt += 1
        elif temp != x:
            length = length + str(temp) + str(cnt)
            temp = x
            cnt = 1

    return length



print(len(chk(A)))
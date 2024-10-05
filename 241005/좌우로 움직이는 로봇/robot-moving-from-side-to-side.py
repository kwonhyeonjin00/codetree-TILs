def check1(arr):
    cur = 0
    for i in arr:
        if i[1] == 'R':
            for j in range(int(i[0])):
                a3.append(cur+1)
                cur += 1
        elif i[1] == 'L':
            for j in range(int(i[0])):
                a3.append(cur-1)
                cur -= 1

def check2(arr):
    cur = 0
    for i in arr:
        if i[1] == 'R':
            for j in range(int(i[0])):
                a4.append(cur+1)
                cur += 1
        elif i[1] == 'L':
            for j in range(int(i[0])):
                a4.append(cur-1)
                cur -= 1
n, m = map(int, input().split())

arr1 = [input().split() for _ in range(n)]
arr2 = [input().split() for _ in range(m)]

a3 = [0]
a4 = [0]

check1(arr1)
check2(arr2)

cnt = 0

if len(a3)>len(a4):
    for i in range(len(a3)-len(a4)):
        a4.append(a4[-1])
elif len(a3)<len(a4):
    for i in range(len(a4)-len(a3)):
        a3.append(a3[-1])

for i in range(1, len(a3)):
    if a3[i] == a4[i] and a3[i-1] != a4[i-1]:
        cnt += 1
print(cnt)
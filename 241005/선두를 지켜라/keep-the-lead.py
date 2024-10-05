def check1(arr):
    cur = 0
    for i in arr:
        for j in range(int(i[1])):
            a3.append(cur+int(i[0]))
            cur += int(i[0])


def check2(arr):
    cur = 0
    for i in arr:
        for j in range(int(i[1])):
            a4.append(cur+int(i[0]))
            cur += int(i[0])

n, m = map(int, input().split())

arr1 = [input().split() for _ in range(n)]
arr2 = [input().split() for _ in range(m)]

a3 = []
a4 = []

check1(arr1)
check2(arr2)

cnt = 0
if a3[0] > a4[0]:
    fir = 1
else:
    fir = 2

for i in range(1, len(a3)-1):
    if fir == 1 and a3[i] < a4[i]:
        cnt += 1
        fir = 2
    elif fir == 2 and a3[i] > a4[i]:
        cnt += 1
        fir = 1
print(cnt)
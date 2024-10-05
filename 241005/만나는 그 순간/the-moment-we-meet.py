def check1(arr):
    cur = 0
    for i in arr:
        if i[0] == 'R':
            for j in range(int(i[1])):
                a3.append(cur+1)
                cur += 1
        elif i[0] == 'L':
            for j in range(int(i[1])):
                a3.append(cur-1)
                cur -= 1

def check2(arr):
    cur = 0
    for i in arr:
        if i[0] == 'R':
            for j in range(int(i[1])):
                a4.append(cur+1)
                cur += 1
        elif i[0] == 'L':
            for j in range(int(i[1])):
                a4.append(cur-1)
                cur -= 1

n, m = map(int, input().split())

arr1 = [input().split() for _ in range(n)]
arr2 = [input().split() for _ in range(m)]

a3 = []
a4 = []

check1(arr1)
check2(arr2)

for i in range(len(a3)):
    if a3[i] == a4[i]:
        print(i+1)
        break
def f(n):
    arr = []
    for i in range(n):
        arr.append(int(input()))

    lens = []
    cnt = 1

    for i in range(n):
        if i == 0:
            cnt += 1
        elif arr[i] == arr[i - 1]:
            cnt += 1
        else:
            lens.append(cnt)
            cnt = 1
    print(max(lens))

n = int(input())

if n == 1:
    print('1')
else:
    f(n)
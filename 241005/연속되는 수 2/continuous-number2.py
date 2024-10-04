arr = []
temp = []

n = int(input())

num = int(input())
temp.append(num)

if n > 1:
    for i in range(n-1):
        num = int(input())
        if num != temp[0]:
            arr.append(len(temp))
            temp = []
        else:
            temp.append(num)
else:
    arr.append(1)


print(max(arr))
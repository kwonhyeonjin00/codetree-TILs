n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
def chk(arr):
    arr.append(0)
    temp = arr[0]
    cnt = 0
    length = ""
    for x in arr:
        if temp == x:
            cnt += 1
        elif temp != x:
            length = length + str(temp) + str(cnt)
            temp = x
            cnt = 1

    return list(length)

num_list = chk(numbers)
while True:
    num_list = chk(numbers)
    t = len(num_list)
    if chk(num_list) == t:
        break
    else:
        num_list = chk(num_list)

for i in range(len(num_list) - 1, -1, -2):
    if int(num_list[i]) >= m:
        num_list.pop(i)
        num_list.pop(i - 1)

print(len(num_list) // 2)
for i in range(0, len(num_list) - 1, 2):
    print(num_list[i])
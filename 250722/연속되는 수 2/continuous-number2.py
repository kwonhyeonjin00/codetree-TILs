n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
l = 1
l_list = []

for i in range(1, n):

    if arr[i] == arr[i - 1]:
        l += 1

    else:
        l_list.append(l)
        l = 1

print(max(l_list))
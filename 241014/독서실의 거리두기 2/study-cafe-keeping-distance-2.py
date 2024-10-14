n = int(input())
arr = list(input())

arr_index = []
diff = []

for i in range(n):
    if arr[i] == '1':
        arr_index.append(i)
temp = n
for i in range(len(arr_index) - 1):
    t = arr_index[i + 1] - arr_index[i]
    temp = min(temp, t)

if arr_index[0] != 0:
    diff.append(arr_index[0])

for j in range(len(arr_index) - 1):
    x = arr_index[j + 1] - arr_index[j]
    if x != 1:
        diff.append((arr_index[j + 1] - arr_index[j]) // 2)

if arr_index[-1] != n - 1:
    diff.append(n - 1 - arr_index[-1])


print(arr_index)
print(diff)

print(min(max(diff), temp))
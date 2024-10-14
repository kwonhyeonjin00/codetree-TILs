n = int(input())
x = list(input())
arr_index = []
arr_index_diff = []

for i in range(n):
    if x[i] == '1':
        arr_index.append(i)

for j in range(len(arr_index) - 1):
    arr_index_diff.append(arr_index[j + 1] - arr_index[j])

s = arr_index_diff.index(max(arr_index_diff))

arr_index.insert(s + 1, (arr_index[s] + arr_index[s + 1]) // 2)

arr_index_diff2 = []

for k in range(len(arr_index) - 1):
    arr_index_diff2.append(arr_index[k + 1] - arr_index[k])

print(min(arr_index_diff2))
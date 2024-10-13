def check(n, arr1, arr2):

    for i in range(n):
        ans = [0] * (max(arr2) + 1)
        for j in range(n):
            if i == j:
                continue
            for k in range(arr1[j], arr2[j] + 1):
                ans[k] += 1

        if n-1 in ans:
            return "Yes"
    
    return "No"

n = int(input())

arr_x1 = []
arr_x2 = []

for i in range(n):
    a, b = map(int, input().split())
    arr_x1.append(a)
    arr_x2.append(b)

x = check(n, arr_x1, arr_x2)

print(x)
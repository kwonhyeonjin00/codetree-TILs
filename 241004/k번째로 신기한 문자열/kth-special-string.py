n, m, s = input().split()
n, m = int(n), int(m)
arr = [input() for _ in range(n)]
arr.sort()

arr2 = []

while arr:
    x = 0
    for i in range(len(s)):
        if arr[0][i] != s[i]:
            arr.pop(0)
            x = 1
    if x == 0:
        arr2.append(arr.pop(0))
      
print(arr2[m-1])
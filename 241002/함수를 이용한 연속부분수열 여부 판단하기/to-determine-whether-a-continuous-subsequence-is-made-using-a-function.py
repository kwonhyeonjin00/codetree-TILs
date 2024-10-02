def sequence(x, y):
    if x == y:
        return True
    return False    
n1, n2 = map(int, input().split())

arr1 = input().split()
arr2 = input().split()

for i in range(n1 - n2 + 1):
    x = ""
    for j in range(n2):
        x += arr1[i+j]
    y = ""
    for k in arr2:
        y += k
    if sequence(x, y):
        z = 1
        break
    else:
        z = 0

if z == 1:
    print("Yes")
else:
    print("No")
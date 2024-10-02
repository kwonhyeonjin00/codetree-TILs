n1, n2 = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def same(n):
    for i in range(n2):
        if arr1[n+i] != arr2[i]:
            return False
    return True

def sequence(x, y):
    for i in range(n1 - n2 + 1):
        if same(i):
            return True
    return False

if sequence(arr1, arr2):
    print("Yes")
else:
    print("No")
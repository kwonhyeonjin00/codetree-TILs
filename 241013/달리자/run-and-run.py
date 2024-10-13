n = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

cnt = 0

for i in range(n-1):
    t = arr1[i] - arr2[i]
    cnt += t
    arr1[i + 1] += t

print(cnt)
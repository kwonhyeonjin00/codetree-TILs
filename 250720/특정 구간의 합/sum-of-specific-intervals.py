n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def hap():
    for i in range(m):
        temp = 0
        a1, a2 = queries[i][0], queries[i][1] 
        for j in range(a1 - 1, a2):
            temp += arr[j]

        print(temp)
hap()

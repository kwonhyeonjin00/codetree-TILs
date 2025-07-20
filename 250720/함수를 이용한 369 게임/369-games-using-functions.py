a, b = map(int, input().split())

# Please write your code here.
def cal_3(n):
    return n % 3 == 0

def magic_number(n):
    x = list(map(int,str(n)))
    return 3 in x or 6 in x or 9 in x or cal_3(n)

cnt = 0

for i in range(a, b + 1):
    if magic_number(i):
        cnt += 1

print(cnt)
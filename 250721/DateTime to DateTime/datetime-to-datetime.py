a, b, c = map(int, input().split())

# Please write your code here.
def cal(a, b, c):
    m = (b * 60 + c) - (11 * 60 + 11)
    d = a - 11

    return d * 1440 + m

if a != 11 and (b <= 10 or (b == 11 and c <= 10)):
    print(-1)
else:
    print(cal(a, b, c))
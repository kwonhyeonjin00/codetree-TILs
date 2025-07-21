m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

A_index = day_of_the_week.index(A)

def cal(m, d):
    total = 0

    for i in range(1, m):
        total += days[i]
    total += d

    return total

diff = cal(m2, d2) - cal(m1, d1)

ans = 0

ans += diff // 7
diff %= 7

if diff >= A_index:
    ans += 1

print(ans) 
m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

c = 0

if m1 > m2 or (m1 == m2 and m1 > d2):
    m1, d1, m2, d2 = m2, d2, m1, d1
    c = 1
diff = 0

while True:
    if m1 == m2 and d1 == d2:
        break

    d1 += 1
    diff += 1

    if d1 > days[m1]:
        m1 += 1
        d1 = 1
diff %= 7

if c == 1:
    diff *= -1

print(day_of_the_week[diff])
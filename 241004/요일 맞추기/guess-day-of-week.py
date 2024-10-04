def f(a, b, c, d, t):

    elapsed_days = 0
    
    #                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
    num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    while True:
        if a == c and b == d:
            break

        elapsed_days += 1
        b += 1

        if b > num_of_days[a]:
            a += 1
            b = 1
    if t == 0:
        print(days[elapsed_days % 7])
    elif t == 1:
        print(days[-(elapsed_days % 7)])

m1, d1, m2, d2 = map(int, input().split())

if m1 > m2:
    f(m2, d2, m1, d1, 1)

elif m1 == m2:
    if d1 > d2:
        f(m2, d2, m1, d1, 1)
    else:
        f(m1, d1, m2, d2, 0)
else:
    f(m1, d1, m2, d2, 0)
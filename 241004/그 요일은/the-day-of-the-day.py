def f(a, b, c, d, e):
    day1 = b
    day2 = d

    #                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
    num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    for i in range(1, a):
        day1 += num_of_days[i]

    for j in range(1, c):
        day2 += num_of_days[j]

    diff = day2 - day1
    cnt = diff // 7
    diff %= 7
    
    if days.index(e) <= diff:
        cnt += 1
    print(cnt)


m1, d1, m2, d2 = map(int, input().split())
s = input()
f(m1, d1, m2, d2, s)
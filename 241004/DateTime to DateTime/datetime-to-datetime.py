def f(a, b, c):
    day, hour, minute = 11, 11, 11
    elapsed_time = 0

    while True:
        if day == a and hour == b and minute == c:
            break

        elapsed_time += 1
        minute += 1

        if minute == 60:
            hour += 1
            minute = 0
        if hour == 24:
            day += 1
            hour = 0

    print(elapsed_time)


a, b, c = map(int, input().split())
if a > 11:
    f(a, b, c)
else:
    if b > 11:
        f(a, b, c)
    elif b == 11:
        if c >= 11:
            f(a, b, c)
        else:
            print("-1")
    elif b < 11:
        print("-1")
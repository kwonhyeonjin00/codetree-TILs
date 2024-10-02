def year(n):
    if n % 400 == 0:
        return True
    elif n % 4 == 0 and n % 100 != 0:
        return True
    return False
    
def YMD(Y, M, D):
    a31 = [1, 3, 5, 7, 8, 10, 12]
    a30 = [4, 6, 9, 11]
    if M in a31 and D <= 31:
        if M == 1 or M == 12:
            return "Winter"
        elif M == 3 or M == 5:
            return "Spring"
        elif M == 7 or M == 8:
            return "Summer"
        elif M == 10:
            return "Fall"

    elif M in a30 and D <= 30:
        if M == 4:
            return "Spring"
        elif M == 6:
            return "Summer"
        elif M == 9 or M == 11:
            return "Fall"

    elif M == 2:
        if year(Y) and D <= 29:
            return "Winter"
        elif year(Y) == False and D <= 28:
            return "Winter"

    return -1

Y, M, D = map(int, input().split())
print(YMD(Y, M, D))
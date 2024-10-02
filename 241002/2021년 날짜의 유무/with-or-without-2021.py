def MD(M, D):
    a31 = [1, 3, 5, 7, 8, 10, 12]
    a30 = [4, 6, 9, 11]
    if M in a31:
        if D <= 31:
            return True
        else:
            return False
    elif M in a30:
        if D <= 30:
            return True
        else:
            return False
    elif M == 2:
        if D <= 28:
            return True
        else:
            return False
    return False


M, D = map(int, input().split())

if MD(M, D):
    print("Yes")
else:
    print("No")
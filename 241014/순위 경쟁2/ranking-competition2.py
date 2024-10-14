n = int(input())
A, B = 0, 0
first = ['Z']

cnt = 0

for i in range(n):
    c, s = input().split()
    s = int(s)
    if c == "A":
        A += s
    elif c == "B":
        B += s

    if A > B:
        fir = ['A']
    elif A < B:
        fir = ['B']
    elif A == B:
        fir = ['A', 'B']

    if first != fir:
        cnt += 1
        first = fir

print(cnt)
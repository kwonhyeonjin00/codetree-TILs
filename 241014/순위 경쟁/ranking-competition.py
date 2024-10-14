n = int(input())
first = [0, 0, 0]
score = [0, 0, 0]

cnt = 0

for i in range(n):
    fir = [0, 0, 0]
    c, s = input().split()
    s = int(s)
    if c == "A":
        score[0] += s
    elif c == "B":
        score[1] += s
    elif c == "C":
        score[2] += s
    if s != 0:
        for i in range(3):
            if score[i] == max(score):
                fir[i] = 1

    if first != fir:
        cnt += 1
        first = fir

print(cnt)
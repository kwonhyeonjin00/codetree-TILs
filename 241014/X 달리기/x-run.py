def min_move(n):
    t = 0
    for i in range(n):
        t += i
    return t

n = int(input())

s = 0
v = 1
time = 0

while True:
    if s == n:
        break
    
    s += v

    move = min_move(v)
    tx = n - s - move

    if tx > v:
        v += 1
    elif tx < v:
        if v > 1:
            v -= 1

    time += 1

print(time)
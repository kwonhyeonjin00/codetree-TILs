def min_move(n):
    t = 0
    for i in range(n):
        t += i
    return t

def max_move(n):
    t = 0
    for i in range(n + 2):
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
    time += 1

    move = min_move(v)
    tx = n - s - move

    if tx > v:
        if max_move(v) <= tx:
            v += 1
    elif tx < v:
        if v > 1:
            v -= 1

print(time)
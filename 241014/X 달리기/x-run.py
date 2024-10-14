def min_move(n):
    t = 0
    for i in range(n):
        t += i
    return t

def same_move(n):
    t = 0
    for i in range(n + 1):
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

    min_m = min_move(v)
    same_m = same_move(v)
    max_m = max_move(v)
    
    tx = n - s

    if tx == min_m or tx < same_m:
        if v > 1:
            v -= 1
    elif max_m <= tx:
        v += 1
        
print(time)
n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.
def push(lst, d):
    if d == 'R':
        lst.append(lst.pop(0))
    elif d == 'L':
        lst.insert(0, lst.pop())
    return lst

def chk(lst_1, lst_2):
    for i in range(len(lst_1)):
        if lst_1[i] == lst_2[i]:
            return True

for i in range(q):
    r, d = winds.pop(0)
    r -= 1 #인덱스 조정 0부터 시작하도록

    a[r] = push(a[r], d)

    r1, r2 = r, r
    d1, d2 = d, d
    
    while r1 > 0 and chk(a[r1], a[r1 - 1]):
        r1 -= 1

        if d1 == 'R':
            d1 = 'L'
        else:
            d1 = 'R'
        
        a[r1] = push(a[r1], d1)

    while r2 < n - 1 and chk(a[r2], a[r2 + 1]):
        r2 += 1

        if d2 == 'R':
            d2 = 'L'
        else:
            d2 = 'R'

        a[r2] = push(a[r2], d2)

for row in a:
    for elem in row:
        print(elem, end=' ')
    print()        
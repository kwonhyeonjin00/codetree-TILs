n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
stack = [0 for _ in range(2000)]

pos = 1000

for i in range(n):
    for j in range(x[i]):
        
        if dir[i] == 'R':
            pos += 1
        else:
            pos -= 1

        stack[pos] += 1
cnt = 0

for k in range(2000):
    if stack[k] >= 2:
        cnt += 1

print(cnt)
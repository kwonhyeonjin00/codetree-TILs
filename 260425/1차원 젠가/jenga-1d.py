n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
blocks = blocks[:s1-1] + blocks[e1:]
blocks = blocks[:s2-1] + blocks[e2:]

if blocks:
    print(len(blocks))
    for x in blocks:
        print(x)
else:
    print(0)
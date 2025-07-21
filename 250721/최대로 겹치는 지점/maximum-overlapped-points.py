n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
stack = [0 for _ in range(101)]

for a, b in segments:
    for i in range(a, b + 1):
        stack[i] += 1

print(max(stack))
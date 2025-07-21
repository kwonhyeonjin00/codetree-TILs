n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
class Number:
    def __init__(self, order, num):
        self.order, self.num = order, num

number = []

for i in range(n):
    number.append(Number(i + 1, sequence[i]))

number.sort(key=lambda x: (x.num, x.order))

ans = [0 for _ in range(n + 1)]

for rank, t in enumerate(number, start=1):
    ans[t.order] = rank

for j in range(1, n + 1):
    print(ans[j], end=' ')
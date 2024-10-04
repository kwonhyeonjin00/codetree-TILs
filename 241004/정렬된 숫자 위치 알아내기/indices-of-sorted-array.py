class Sequence:
    def __init__(self, num, number):
        self.num = num
        self.number = number

n = int(input())
arr = list(map(int, input().split()))

sequence = []
for i in range(n):
    sequence.append(Sequence(arr[i], i+1))

sequence.sort(key=lambda x: x.num)

for i in range(1, n+1):
    for j in range(n):
        if sequence[j].number == i:
            print(j+1, end=' ')
            break
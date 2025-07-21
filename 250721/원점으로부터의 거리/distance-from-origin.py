n = int(input())
points = [(int(i + 1), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
class Distance:
    def __init__(self, number, d_x, d_y):
        self.number, self.d_x, self.d_y = number, d_x, d_y

distance = []

for i in range(n):
    distance.append(Distance(points[i][0], points[i][1][0], points[i][1][1]))

distance.sort(key=lambda x: (x.d_x ** 2 + x.d_y ** 2, x.number))

for t in distance:
   print(t.number)
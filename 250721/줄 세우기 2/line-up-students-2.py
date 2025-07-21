n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
class Student:
    def __init__(self, height, weight, number):
        self.height, self.weight, self.number = height, weight, number

student = []

for i in range(n):
    student.append(Student(students[i][0], students[i][1], students[i][2]))

student.sort(key=lambda x: (x.height, -x.weight))

for t in student:
    print(t.height, t.weight, t.number)
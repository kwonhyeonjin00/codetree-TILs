n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.
class Score:
    def __init__(self, name, score1, score2, score3):
        self.name, self.score1, self.score2, self.score3 = name, score1, score2, score3

score = []

for i in range(n):
    score.append(Score(name[i], score1[i], score2[i], score3[i]))

score.sort(key=lambda x: x.score1 + x.score2 + x.score3)

for t in score:
    print(t.name, t.score1, t.score2, t.score3)
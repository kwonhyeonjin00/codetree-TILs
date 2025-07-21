n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
class Score:
    def __init__(self, name, kor, eng, math):
        self.name, self.kor, self.eng, self.math = name, kor, eng, math

score = []

for i in range(n):
    score.append(Score(name[i], korean[i], english[i], math[i]))

score.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

for t in score:
    print(t.name, t.kor, t.eng, t.math)
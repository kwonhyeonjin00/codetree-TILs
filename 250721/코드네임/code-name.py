MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Member:
    def __init__(self, name, score):
        self.name = name
        self.score = score

member = []

min_score = 101

for i in range(MAX_N):
    member.append(Member(codenames[i], scores[i]))

for i in range(MAX_N):
    if member[i].score < min_score:
        min_score = member[i].score
        x = i

print(member[x].name, member[x].score)
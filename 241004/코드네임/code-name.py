class Spy:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

Spys = []
for _ in range(5):
    codename, score = tuple(map(str, input().split()))
    score = int(score)
    Spys.append(Spy(codename, score))

min = Spys[0].score
idx = 0
for i in range(1, 5):
    if Spys[i].score < min:
        idx = i

print(Spys[idx].codename, Spys[idx].score)
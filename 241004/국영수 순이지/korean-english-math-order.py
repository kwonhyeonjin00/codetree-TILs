class People:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())

people = []
for i in range(n):
    name, kor, eng, math = input().split()
    kor, eng, math = int(kor), int(eng), int(math)
    people.append(People(name, kor, eng, math))

people.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

for x in people:
    print(f'{x.name} {x.kor} {x.eng} {x.math}')
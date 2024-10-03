class Game:
    def __init__(self, Id, Level):
        self.Id = Id
        self.Level = Level

Game1 = Game('codetree', 10)

Id, Level = input().split()
Game2 = Game(Id, Level)

print(f'user {Game1.Id} lv {Game1.Level}')
print(f'user {Game2.Id} lv {Game2.Level}')
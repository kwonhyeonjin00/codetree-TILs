class Spy:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

code, color, second = tuple(map(str, input().split()))

spy1 = Spy(code, color, second)

print(f'code : {spy1.code}')
print(f'color : {spy1.color}')
print(f'second : {spy1.second}')
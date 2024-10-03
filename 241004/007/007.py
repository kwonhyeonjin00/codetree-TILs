class Secret:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

code, place, time = input().split()
Secret1 = Secret(code, place, time)

print(f'secret code : {Secret1.code}')
print(f'meeting point : {Secret1.place}')
print(f'time : {Secret1.time}')
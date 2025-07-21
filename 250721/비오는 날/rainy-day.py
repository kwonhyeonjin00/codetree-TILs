n = int(input())
dates = []
days = []
weathers = []

for _ in range(n):
    d, dy, w = input().split()
    dates.append(d)
    days.append(dy)
    weathers.append(w)

# Please write your code here.
class Infor:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

infor = []

for i in range(n):
    infor.append(Infor(dates[i], days[i], weathers[i]))

da = '2100-00-00'
index = 0

for i in range(n):
    if infor[i].weather == "Rain":
        if infor[i].date < da:
            da = infor[i].date
            index = i

print(f"{infor[index].date} {infor[index].day} {infor[index].weather}")
class Data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

dates = []

data = []
for i in range(n):
    date, day, weather = input().split()
    data.append(Data(date, day, weather))
    if weather == "Rain":
        dates.append([date, i])

dates.sort()
idx = dates[0][1]

print(f'{data[idx].date} {data[idx].day} {data[idx].weather}')
class Weather:
    def __init__(self, date, day, state):
        self.date = date
        self.day = day
        self.state = state

    def __str__(self):
        return "{date} {day} {state}".format(date=self.date, day=self.day, state=self.state)

n = int(input())

weathers = []

for _ in range(n):
    weathers.append(Weather(*input().split()))

weathers = sorted(weathers, key=lambda weather: weather.date)

for elem in weathers:
    if elem.state == "Rain":
        print(elem)
        break
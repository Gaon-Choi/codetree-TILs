month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

m1, d1, m2, d2 = map(int, input().split())

day_1 = month[m1 - 1] + d1
day_2 = month[m2 - 1] + d2

print(weekday[(day_2 - day_1) % 7])
is_leap_year = True

month = [0, 31, 28 + (1 if is_leap_year else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

m1, d1, m2, d2 = map(int, input().split())
day = weekday.index(input())

day_1 = sum(month[0 : m1]) + d1
day_2 = sum(month[0 : m2]) + d2

result = 0

for i in range(day_1, day_2 + 1):
    if i % 7 == day:
        result += 1

print(result)
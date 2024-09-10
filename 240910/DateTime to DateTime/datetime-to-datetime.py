a, b, c = map(int, input().split())

HOUR = 60
DAY = HOUR * 24

current = DAY * a + HOUR * b + c
eleven = DAY * 11 + HOUR * 11 + 11

if current - eleven > 0:
    print(current - eleven)
else:
    print(-1)
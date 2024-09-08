cnt = 0

n = int(input())

for year in range(1, n + 1):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            continue
        else:
            cnt += 1

print(cnt)
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())

cnt = 1

while (not (m1 == m2 and d1 == d2)):
    if num_of_days[m1] == d1:
        d1 = 1
        m1 += 1
    else:
        d1 += 1

    cnt += 1

print(cnt)
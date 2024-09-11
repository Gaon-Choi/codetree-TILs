Y, M, D = map(int, input().split())

is_leap_year = None

if Y % 4 == 0:
    if Y % 100 == 0:
        if Y % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False


month = [0, 31, 28 + (1 if is_leap_year else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month[M] < D:
    print(-1)
    exit(0)
else:
    if 3 <= M and M <= 5:
        print("Spring")
    elif 6 <= M and M <= 8:
        print("Summer")
    elif 9 <= M and M <= 11:
        print("Fall")
    else:
        print("Winter")
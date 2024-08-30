year = int(input())

if year % 100 == 0 and year % 400 != 0:
    print('false')
elif year % 4 != 0:
    print('false')
else:
    print('true')
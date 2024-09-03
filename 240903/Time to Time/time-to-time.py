a, b, c, d = map(int, input().split())

minute = 0

while (not (a == c and b == d)):
    if b + 1 == 60:
        b = 0
        a += 1
    else:
        b += 1
    
    minute += 1

print(minute)
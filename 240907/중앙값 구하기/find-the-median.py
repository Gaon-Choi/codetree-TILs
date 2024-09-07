a, b, c = map(int, input().split())

if a > b:
    if c > a:
        print(a)
    else:
        if b > c:
            print(b)
        else:
            print(c)
else:
    #a < b
    if c > b:
        print(b)
    else:
        #a < b, c < b
        if a > c:
            print(a)
        else:
            print(c)
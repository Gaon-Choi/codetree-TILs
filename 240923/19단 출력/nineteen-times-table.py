dan = 19

for i in range(1, dan+1):
    for j in range(1, dan+1):
        print("{a} * {b} = {result}".format(a=i, b=j, result=i*j), end=" ")
        if j % 2 == 0:
            print()
        elif j < dan:
            print("/", end=" ")
    print()
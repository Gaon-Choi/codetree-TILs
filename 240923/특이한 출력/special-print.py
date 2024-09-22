n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        print("({a}, {b})".format(a=i, b=j), end=" ")
        if (i + j) % 4 == 0:
            print()
            #break
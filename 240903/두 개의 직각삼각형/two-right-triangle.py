N = int(input())

space = 0

for i in range(N, 0, -1):
    print("*" * i, " " * (2 * space), "*" * i, sep="")
    space += 1
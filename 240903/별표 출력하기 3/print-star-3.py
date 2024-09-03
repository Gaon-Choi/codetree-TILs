N = int(input())

space = 0

for i in range(N, 0, -1):
    print("  " * space, "* " * (2 * i - 1), sep="")
    space += 1
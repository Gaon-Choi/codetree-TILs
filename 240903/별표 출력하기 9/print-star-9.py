N = int(input())

space = N - 1

for i in range(N):
    print("  " * space, "* " * (2 * i + 1), sep="")
    space -= 1
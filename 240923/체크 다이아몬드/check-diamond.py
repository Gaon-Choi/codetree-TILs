n = int(input())

space = n - 1

for i in range(1, n + 1):
    print(" " * space, "* " * i, sep="")
    space -= 1

space += 2

for i in range(n - 1, 0, -1):
    print(" " * space, "* " * i, sep="")
    space += 1
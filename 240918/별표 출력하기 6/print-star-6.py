n = int(input())

side = n - 1
blank = 0

for _ in range(n):
    print("  " * blank, "* " * side, "* ", "* " * side, "  " * blank, sep="")
    side -= 1
    blank += 1

side += 2
blank -= 2

for _ in range(1, n):
    print("  " * blank, "* " * side, "* ", "* " * side, "  " * blank, sep="")
    side += 1
    blank -= 1
n = int(input())

blank = n - 1
star = 1

for _ in range(n):
    print("  " * blank, "@ " * star, sep="")
    blank -= 1
    star += 1

blank += 2
star -= 2

for _ in range(1, n):
    print("@ " * star, "  " * blank, sep="")
    blank += 1
    star -= 1
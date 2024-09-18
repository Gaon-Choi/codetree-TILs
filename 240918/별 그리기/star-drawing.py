n = int(input())

blank = n - 1
star = 0

for _ in range(n):
    print(" " * blank, "*" * star, "*", "*" * star, sep="")
    star += 1
    blank -= 1

star -= 2
blank += 2

for _ in range(1, n):
    print(" " * blank, "*" * star, "*", "*" * star, sep="")
    star -= 1
    blank += 1
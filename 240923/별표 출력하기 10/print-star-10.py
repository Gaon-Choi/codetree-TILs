n = int(input())

for i in range(2 * n):
    if i % 2 == 0:
        print("* " * (1 + (i // 2)))
    else:
        print("* " * (n - (i - 1) // 2))